DROP TABLE IF EXISTS `timestamp`;
CREATE TABLE `timestamp` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `dep_set_id`  varchar(30)  not null default '',
  `mtime`       decimal(20,2)  not null default 0.0,
  `event`       varchar(8)  default '',
  `info1`        varchar(128)  default '',
  `info2`        varchar(128)  default '',
  `info3`        varchar(20)  default '',
  `info4`        varchar(20)  default '',
  PRIMARY KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=latin1;

create index dep_idtime on user_data (dep_set_id);

