alter table deposition add column country varchar(32) not null default '';
alter table deposition add column nmolecule integer not null default -1;
alter table user_data add column country varchar(32) not null default '';

CREATE TABLE `related_db` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `dep_set_id`  varchar(30)  not null default '',
  `id_code`     varchar(20)  default '',
  `id_db`       varchar(20)  default '',
  PRIMARY KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=latin1;

create index dep_idrelated on related_db (dep_set_id);

CREATE TABLE `other_data` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `dep_set_id`  varchar(30)  not null default '',
  `data`        varchar(64)  default '',
  `code`        varchar(64)  default '',
  PRIMARY KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=latin1;

create index dep_idother on other_data (dep_set_id);

CREATE TABLE `experiments_db` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `dep_set_id`  varchar(30)  not null default '',
  `expt`        varchar(20)  default '',
  PRIMARY KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=latin1;

create index dep_idexpt on experiments_db (dep_set_id);

CREATE TABLE `codes_db` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `dep_set_id`  varchar(30)  not null default '',
  `code`        varchar(20)  default '',
  PRIMARY KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB AUTO_INCREMENT=48 DEFAULT CHARSET=latin1;

create index dep_idcodes on codes_db (dep_set_id);

