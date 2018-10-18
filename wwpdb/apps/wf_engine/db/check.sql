select deposition.dep_set_id,pdb_id, depPW, user_data.email,last_name from user_data,deposition where user_data.dep_set_id = deposition.dep_set_id
