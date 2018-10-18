alter table deposition add column emdb_id varchar(9) default NULL;

DROP TABLE IF EXISTS `emdbID`;
CREATE TABLE `emdbID` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `emdb_id` varchar(9) DEFAULT NULL,
  `used` varchar(2) DEFAULT 'n',
  PRIMARY KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=latin1;

create unique index emdbindexid on emdbID (emdb_id);
create unique index emdbindexord on emdbID (ordinal);

alter table deposition add column bmrb_id varchar(6) default NULL;

DROP TABLE IF EXISTS `bmrbID`;
CREATE TABLE `bmrbID` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `bmrb_id` varchar(6) DEFAULT NULL,
  `used` varchar(2) DEFAULT 'n',
  PRIMARY KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=latin1;

create unique index bmrbindexid on bmrbID (bmrb_id);
create unique index bmrbindexord on bmrbID (ordinal);
