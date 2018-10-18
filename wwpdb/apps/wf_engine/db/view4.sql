  select distinct `d1`.`dep_set_id` AS `dep_set_id`,
                  `d1`.`pdb_id` AS `pdb_id`,
                  `d1`.`dep_initial_deposition_date` AS `dep_initial_deposition_date`,
                  `d1`.`annotator_initials` AS `annotator_initials`,
                  `d1`.`dep_deposit_site` AS `dep_deposit_site`,
                  `d1`.`dep_process_site` AS `dep_process_site`,
                  `d1`.`dep_status_code` AS `dep_status_code`,
                  `d1`.`inst_owner` AS `inst_owner`,
                  `d1`.`inst_status` AS `inst_status`,
                  `d1`.`inst_status_timestamp` AS `inst_status_timestamp`
  from (`dep_instance` `d1` join `dep_instance` `d2`) 
  where ((`d1`.`dep_set_id` = `d2`.`dep_set_id`) and 
         (`d1`.`inst_status_timestamp` = (select max(`d2`.`inst_status_timestamp`) AS `max(d2.inst_status_timestamp)` 
     from `dep_instance` `d2` 
     where (`d2`.`dep_set_id` = `d1`.`dep_set_id`)))) 
