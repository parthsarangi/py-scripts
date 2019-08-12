#!/usr/bin/env bash

for view in $(cat view_list)
do
  echo "reading :" $view
  bq show --schema mm_datamart.$view > file_$view
  bq show --view mm_datamart_view.$view > sql_$view
done
