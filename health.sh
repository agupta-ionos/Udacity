#!/bin/bash
########################################################################################
#Script Name	:health.sh							       #
#Description	:Script that fetches metrics values of all resources used per K8s Node #
#Author       	:Anubhav Gupta 							       #
#Email         	:anubhav.25gupta@gmail.com					       #
#										       #
# [DEBUG OPTION]								       #
#    set -x  # Comment this line to stop debugging this shell script          	       #
#										       #
########################################################################################


#Creating a logging file which merges all the output to  filename - logoutput.
LOGFILE=${HOME}/logs/logouput

#Creating a logging file which creates log file on timestamp basis under log folder.
LOG=${HOME}/logs/node_status.$(date +%Y%m%d%H%M).log
(
echo "=================================================================" >> $LOGFILE 2>&1
echo "`date +%H:%M:%S` : Started Fetching K8s Metrics at this Timestamp" >> $LOGFILE 2>&1
echo "=================================================================" >> $LOGFILE 2>&1

#Function to check existence of kubectl CLI tool on K8 Cluster
error_handling() {

#Enabling Logging
set -x

message=""
KUBECTL="kubectl"

#Storing the output of this command into error.txt
$KUBECTL version 2>&1 | tee error.txt

#Checking for kubectl binary file i.e. the main installation file in bin folder.
ls -lrt /usr/local/bin/kubectl
status=$?
if [ $status -eq 0 ]; then
    error_code
else
    echo Kubectl not found! Install kubectl properly!
    break
fi
}

#Function to handle the error codes based on the standard errors that pop out during kubectl command runnning
error_code() {

error1="kubectl: command not found"
error2="The connection to the server localhost:8080 was refused - did you specify the right host or port?"
error3="No resources found."
error4="Error: ErrImagePull"

message=$( cat ./error.txt )
#Checking only for kubectl not found error code. Error handling can be set on another codes too
if [  "*$message*" == "*$error1*"  ]; then
	echo Kubectl is not installed properly. Install Kubectl properly
else
	get_nodes
fi

}


#Function to fetch metrics values of all resources used per K8s Node i.e. Resources (CPU, memory, requests), Allocatable resources etc.
get_nodes() {

set -x

echo -e "Getting Status of the Kubernetes Nodes\n"

nodes=$($KUBECTL get nodes --no-headers -o custom-columns=NAME:.metadata.name)

for node in $nodes; do
  echo "Node: $node"
  kubectl describe node "$node" | sed '1,/Non-terminated Pods/d' >> status.txt
  kubectl describe node "$node" | sed '1,/Non-terminated Pods/d' >> $LOGFILE 2>&1
  echo
done
txt2html --make_table --infile "status.txt" --outfile "status.html"
pandoc status.html -V geometry:"paperwidth=300mm, paperheight=300mm, margin=2pt" -t latex -o status.pdf

echo "===============================================================" >> $LOGFILE 2>&1
echo "`date +%H:%M:%S` : Finished getting K8 metric at this Timestamp" >> $LOGFILE 2>&1
echo "===============================================================" >> $LOGFILE 2>&1

}

error_handling
) | tee $LOG
