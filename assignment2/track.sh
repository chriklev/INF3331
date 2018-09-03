#!/bin/bash
LANG=en_us_8859_1

LOGFILE="LOGFILE.txt"
lastLine=$( tail -n 1 $LOGFILE )

case $1 in

  "start")  if [[ $lastLine == "" ]]; then
               echo "START...$(date)" >> $LOGFILE
               echo "LABEL...${2}" >> $LOGFILE
               echo "Succesfully started new task."
            else
               echo "There is alreay an active task. You need to stop the task before creating a new one!"
            fi
  ;;

  "stop")   if [[ $lastLine != "" ]]; then
                echo "STOP....$(date)" >> $LOGFILE
                echo "" >> $LOGFILE
                echo "Succesfully stopped task."
            else
                echo "There is no active task to stop."
            fi
  ;;

  "status") if [[ $lastLine != "" ]]; then
                echo "Active task: ${lastLine:8}"
            else
                echo "There is no active task."
            fi
  ;;

  "log")    echo "All tasks and time elapsed in HH:MM:SS:"
            i=0;d1="";d2="";label=""
            while IFS='$LOGFILE' read -r line; do
                case $(( i%4 )) in
                  0) d1=$(date -d "${line:8}" +%s)
                  ;;
                  1) label=${line:8}
                  ;;
                  2) d2=$(date -d "${line:8}" +%s)
                  ;;
                  3) echo "...${label}: $(date -d @"$(( $d2-$d1-3600 ))" +%T)"
                  ;;
                  *) echo "script not working as inteded"
                esac
                i=$i+1
            done < $LOGFILE
  ;;

  *)        echo "Allowed arguments"
            echo "start:  takes a string and startes a new task with the string as a label."
            echo "stop:   stops the active task."
            echo "status: prints the label of the active task."
            echo "log:    prints the properties of all the tasks."
esac
