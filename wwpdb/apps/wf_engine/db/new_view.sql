CREATE OR REPLACE VIEW dep_last_instance AS (
  select `deposition`.`dep_set_id` AS `dep_set_id`,
                  `deposition`.`pdb_id` AS `pdb_id`,
                  `deposition`.`initial_deposition_date` AS `dep_initial_deposition_date`,
                  `deposition`.`annotator_initials` AS `annotator_initials`,
                  `deposition`.`deposit_site` AS `dep_deposit_site`,
                  `deposition`.`process_site` AS `dep_process_site`,
                  `deposition`.`status_code` AS `dep_status_code`,
                  `deposition`.`author_release_status_code` AS `dep_author_release_status_code`,
                  `deposition`.`title` AS `dep_title`,
                  `deposition`.`author_list` AS `dep_author_list`,
                  `deposition`.`exp_method` AS `dep_exp_method`,
                  `deposition`.`status_code_exp` AS `dep_status_code_exp`,
                  `deposition`.`SG_center` AS `dep_SG_center`,
                  `wf_instance_last`.`ordinal` AS `inst_ordinal`,
                  `wf_instance_last`.`wf_inst_id` AS `inst_id`,
                  `wf_instance_last`.`owner` AS `inst_owner`,
                  `wf_instance_last`.`inst_status` AS `inst_status`,
                  `wf_instance_last`.`status_timestamp` AS `inst_status_timestamp`,
                  `wf_instance_last`.`wf_class_id` AS `class_id`,
                  `wf_class_dict`.`wf_class_name` AS `class_name`,
                  `wf_class_dict`.`title` AS `class_title`,
                  `wf_class_dict`.`author` AS `class_author`,
                  `wf_class_dict`.`version` AS `class_version`,
                  `wf_class_dict`.`class_file` AS `class_file`
  from `deposition`  , `wf_instance_last` , `wf_class_dict` 
  where deposition.dep_set_id = wf_instance_last.dep_set_id
    and wf_instance_last.wf_class_id = wf_class_dict.wf_class_id
);
