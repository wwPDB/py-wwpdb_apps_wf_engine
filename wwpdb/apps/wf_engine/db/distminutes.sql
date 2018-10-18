select minutes,count(1) from (select round(convert(t9.status_timestamp - t1.status_timestamp,signed)/60) as minutes from 
  (select dep_set_id, wf_inst_id, wf_class_id, task_name, status_timestamp from wf_task where task_name = 'T1') as t1 , 
  (select dep_set_id, wf_inst_id, wf_class_id, task_name, status_timestamp from wf_task where task_name = 'T9') as t9  
where t9.dep_set_id = t1.dep_set_id and t9.wf_inst_id = t1.wf_inst_id and t9.wf_class_id = t1.wf_class_id) as minutes
group by minutes
order by minutes
