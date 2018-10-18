alter table deposition add column email varchar(64) not null default '';
DROP TABLE IF EXISTS `user_data`;
CREATE TABLE `user_data` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `dep_set_id`  varchar(30)  not null default '',
  `email`       varchar(64)  not null default '',
  `last_name`   varchar(64)  default '',
  `role`        varchar(8)  default '',
  PRIMARY KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=latin1;

create index dep_id on user_data (dep_set_id);

