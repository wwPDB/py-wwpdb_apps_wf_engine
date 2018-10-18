DROP TABLE IF EXISTS `status_change`;
CREATE TABLE `status_change` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `dep_set_id`  varchar(30)  not null default '',
  `mtime`       decimal(20,2)  not null default 0.0,
  `laststatus`  varchar(10)  not null default '',
  `status`      varchar(10)  not null default '',
  `annotator`   varchar(10)  default 'unknown',
  `owner`       varchar(10)  default 'unknown',
  `module`      varchar(10)  default 'unknown',
  PRIMARY KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=latin1;

create index dep_status_id on status_change (dep_set_id);

