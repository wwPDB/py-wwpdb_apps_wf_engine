SELECT d.dep_set_id,d.pdb_id,d.dep_initial_deposition_date,d.annotator_initials,d.dep_deposit_site,d.dep_process_site,
       d.dep_status_code,d.dep_author_release_status_code,d.dep_title,d.dep_author_list,d.dep_exp_method,
       d.dep_status_code_exp,d.dep_SG_center,d.deppw,d.dep_notify,d.dep_locking,
       d.inst_ordinal, d.inst_id, d.inst_owner, d.inst_status, d.inst_status_timestamp, 
       d.class_id, d.class_name, d.class_title, d.class_author, d.class_version, d.class_file
       FROM dep_last_instance as d  WHERE     d.dep_status_code = "WAIT"  order by d.dep_set_id limit 100
