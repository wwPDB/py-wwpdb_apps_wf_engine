    SELECT
      DISTINCT dep_instance_1.dep_set_id,
               dep_instance_1.pdb_id,
               dep_instance_1.dep_initial_deposition_date,
               dep_instance_1.annotator_initials,
               dep_instance_1.dep_deposit_site,
               dep_instance_1.dep_process_site,
               dep_instance_1.dep_status_code,
               dep_instance_1.dep_author_release_status_code,
               dep_instance_1.dep_title,
               dep_instance_1.dep_author_list,
               dep_instance_1.dep_exp_method,
               dep_instance_1.dep_status_code_exp,
               dep_instance_1.dep_SG_center,
               dep_instance_1.inst_ordinal,
               dep_instance_1.inst_id,
               dep_instance_1.inst_owner,
               dep_instance_1.inst_status,
               dep_instance_1.inst_status_timestamp,
               dep_instance_1.class_id,
               dep_instance_1.class_name,
               dep_instance_1.class_title,
               dep_instance_1.class_author,
               dep_instance_1.class_version,
               dep_instance_1.class_file
    FROM
      dep_instance AS dep_instance_1
    JOIN
      (
        SELECT
          dep_set_id,
          max(inst_status_timestamp) AS inst_status_timestamp
        FROM
          dep_instance AS dep_instance_2
        GROUP BY
          dep_set_id
      ) AS dep_instance_max_timestamp
      ON
        dep_instance_1.dep_set_id = dep_instance_max_timestamp.dep_set_id AND
        dep_instance_1.inst_status_timestamp = dep_instance_max_timestamp.inst_status_timestamp;
