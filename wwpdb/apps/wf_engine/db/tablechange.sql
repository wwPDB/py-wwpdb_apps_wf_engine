ALTER TABLE author_corrections MODIFY dep_set_id varchar(30);
ALTER TABLE communication MODIFY dep_set_id varchar(30);
ALTER TABLE communication MODIFY parent_dep_set_id varchar(30);
ALTER TABLE contact_author MODIFY dep_set_id varchar(30);
ALTER TABLE database_PDB_obs_spr MODIFY dep_set_id varchar(30);
ALTER TABLE database_ref MODIFY dep_set_id varchar(30);
ALTER TABLE database_related MODIFY dep_set_id varchar(30);
ALTER TABLE dep_instance MODIFY dep_set_id varchar(30);
ALTER TABLE dep_last_instance MODIFY dep_set_id varchar(30);
ALTER TABLE dep_with_problems MODIFY dep_set_id varchar(30);
ALTER TABLE deposition MODIFY dep_set_id varchar(30);
ALTER TABLE process_information MODIFY dep_set_id varchar(30);
ALTER TABLE release_request MODIFY dep_set_id varchar(30);
ALTER TABLE wf_instance MODIFY dep_set_id varchar(30);
ALTER TABLE wf_instance_last MODIFY dep_set_id varchar(30);
ALTER TABLE wf_reference MODIFY dep_set_id varchar(30);
ALTER TABLE wf_task MODIFY dep_set_id varchar(30);
