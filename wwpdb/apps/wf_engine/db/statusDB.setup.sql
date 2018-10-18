-- MySQL dump 10.13  Distrib 5.5.3-m3, for unknown-linux-gnu (x86_64)
--
-- Host: localhost    Database: status
-- ------------------------------------------------------
-- Server version	5.5.3-m3-community-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `author_corrections`
--

DROP TABLE IF EXISTS `author_corrections`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `author_corrections` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `dep_set_id` varchar(10) NOT NULL,
  `content` varchar(40) NOT NULL,
  `sending_date` date DEFAULT NULL,
  `remark` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ordinal`),
  KEY `dep_set_id` (`dep_set_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `author_corrections`
--

LOCK TABLES `author_corrections` WRITE;
/*!40000 ALTER TABLE `author_corrections` DISABLE KEYS */;
/*!40000 ALTER TABLE `author_corrections` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `communication`
--

DROP TABLE IF EXISTS `communication`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `communication` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `sender` varchar(10) NOT NULL,
  `receiver` varchar(10) NOT NULL,
  `dep_set_id` varchar(10) NOT NULL,
  `wf_class_id` varchar(10) DEFAULT NULL,
  `wf_inst_id` varchar(10) DEFAULT NULL,
  `wf_class_file` varchar(50) DEFAULT NULL,
  `command` varchar(50) NOT NULL,
  `status` varchar(10) DEFAULT NULL,
  `actual_timestamp` decimal(20,8) DEFAULT NULL,
  `parent_dep_set_id` varchar(10) NOT NULL,
  `parent_wf_class_id` varchar(10) NOT NULL,
  `parent_wf_inst_id` varchar(10) NOT NULL,
  `data_version` varchar(10) DEFAULT NULL,
  `host` varchar(50) DEFAULT NULL,
  `activity` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`ordinal`),
  KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB AUTO_INCREMENT=16151 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `communication`
--

LOCK TABLES `communication` WRITE;
/*!40000 ALTER TABLE `communication` DISABLE KEYS */;
/*!40000 ALTER TABLE `communication` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contact_author`
--

DROP TABLE IF EXISTS `contact_author`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contact_author` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `dep_set_id` varchar(10) NOT NULL,
  `name_salutation` varchar(15) DEFAULT NULL,
  `name_first` varchar(40) NOT NULL,
  `name_last` varchar(65) NOT NULL,
  `name_mi` varchar(50) DEFAULT NULL,
  `role` varchar(50) NOT NULL,
  `email` varchar(255) NOT NULL,
  `address_1` varchar(520) NOT NULL,
  `address_2` varchar(255) DEFAULT NULL,
  `address_3` varchar(255) DEFAULT NULL,
  `city` varchar(60) NOT NULL,
  `state_province` varchar(70) DEFAULT NULL,
  `postal_code` varchar(128) NOT NULL,
  `country` varchar(50) NOT NULL,
  `phone` varchar(60) DEFAULT NULL,
  `fax` varchar(60) DEFAULT NULL,
  `organization_type` varchar(40) NOT NULL,
  PRIMARY KEY (`dep_set_id`,`name_first`,`name_last`),
  KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contact_author`
--

LOCK TABLES `contact_author` WRITE;
/*!40000 ALTER TABLE `contact_author` DISABLE KEYS */;
/*!40000 ALTER TABLE `contact_author` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `da_group`
--

DROP TABLE IF EXISTS `da_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `da_group` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(20) NOT NULL,
  `group_name` varchar(25) NOT NULL,
  `site` varchar(4) NOT NULL,
  `main_page` varchar(30) DEFAULT NULL,
  `da_group_id` int(10) NOT NULL,
  PRIMARY KEY (`da_group_id`),
  KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `da_group`
--

LOCK TABLES `da_group` WRITE;
/*!40000 ALTER TABLE `da_group` DISABLE KEYS */;
INSERT INTO `da_group` VALUES (1,'ADMIN','Administrator','ALL','Admin.html',1),(2,'ANN','Annotator-test','ALL','Annotators.html',2),(3,'ANN','PDBe - Annotator','PDBe','PDBAnnotators.html',3),(4,'ANN','PDBJ - Annotator','PDBj','Annotators.html',4),(5,'ANN','RCSB - Annotator','RCSB','Annotators.html',5),(6,'LANN','RCSB - Lead Annotator','RCSB','RCSBLeadAnnotator.html',6),(7,'LANN','PDBe - Lead Annotator','PDBe','PDBLeadAnnotator.html',7);
/*!40000 ALTER TABLE `da_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `da_users`
--

DROP TABLE IF EXISTS `da_users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `da_users` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(20) NOT NULL,
  `password` varchar(10) NOT NULL,
  `da_group_id` int(10) NOT NULL,
  `email` varchar(50) NOT NULL,
  `initials` varchar(5) DEFAULT NULL,
  `first_name` varchar(50) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `active` int(1) DEFAULT '0',
  PRIMARY KEY (`user_name`),
  KEY `da_group_id` (`da_group_id`),
  KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `da_users`
--

LOCK TABLES `da_users` WRITE;
/*!40000 ALTER TABLE `da_users` DISABLE KEYS */;
INSERT INTO `da_users` VALUES (1,'admin','wman_admin',1,'oldfield@ebi.ac.uk','AD','Admin','Admin',0),(2,'ann','ann',2,'ann@a2nn.com','AN','Ann','Ann',0),(3,'BD','BD',5,'batsal@rcsb.rutgers.edu','BD','Batsal','Devokta',1),(34,'BH','BH',5,'hudson@rcsb.rutgers.edu','BH','Brian','Hudson',0),(35,'BN','BN',5,'buvna@rcsb.rutgers.edu','BN','Buvna','Narayanan',0),(4,'CS','CS',5,'chenghua@rcsb.rutgers.edu','CS','Chenghua',' Shao',0),(5,'EP','EP',5,'peisach@rcsb.rutgers.edu ','EP','Ezra','Peisach',0),(6,'GG','GG',5,'guanghua@rcsb.rutgers.edu ','GG','Guanghua',' Gao',0),(7,'GJS','GJS',3,'jawahar@ebi.ac.uk','GJS','Jawahar','Swaminathan',0),(8,'GS','GS',3,'gaurav@ebi.ac.uk','GS','Gaurav','Sahni',0),(9,'GVG','GVG',3,'glen@ebi.ac.uk','GVG','Glen','van Ginkel',0),(10,'IP','IP',5,'irina@rcsb.rutgers.edu','IP','Irina','Persikova',0),(50,'JW','JW',5,'jwest@rcsb.rutgers.edu','JW','John','Westbrook',0),(48,'JY','JY',5,'jasmin@rcsb.rutgers.edu','JY','Jasmine','Young',0),(13,'KM','KM',4,'matsuura@adit.protein.osaka-u.ac.jp','KM','Kanna','Matsuura',0),(14,'LD','LD',5,'dicostanzo@rcsb.rutgers.edu ','LD','Luigi','Dicostanzo',0),(11,'LEAD','LEAD',6,'jasmin@rcsb.rutgers.edu','LEAD','Jasmine','Young(Lead)',0),(15,'LT','LT',5,'lihua@rcsb.rutgers.edu','LT','Lihua','Tan',0),(44,'luana','rinaldi',5,'luana.rinaldi@gmail.com','LR','luana','rinaldi',1),(16,'MC','MC',3,'conroy@ebi.ac.uk','MC','Matthew','Conroy',0),(46,'MCH','MCH',4,'chen@adit.protein.osaka-u.ac.jp','MCH','Minyu','Chen',0),(17,'MRS','MRS',5,'sekharan@rcsb.rutgers.edu','MRS','Monica','Sekharhan',0),(32,'MS','MS',3,'martyn@ebi.ac.uk','MS','Martyn','Symmons',0),(18,'MZ','MZ',5,'marina@rcsb.rutgers.edu','MZ','Marina','Zhuravleva',0),(22,'pdbjJPN','pdbjJPN',4,'','JPN','unassigned','unassiged',0),(27,'RI','RI',4,'igarashi@adit.protein.osaka-u.ac.jp','RI','Reiko','Igarashi',0),(28,'SG','SG',5,'sutapa@rcsb.rutgers.edu','SG','Sutapa','Ghosh',0),(29,'SS','SS',7,'ssen@ebi.ac.uk','SS','Sanchayita','Sen',0),(49,'TO','TO',5,'oldfield@ebi.ac.uk','TO','Tom','Oldfield',0),(30,'YK','YK',4,'kengau@adit.protein.osaka-u.ac.jp','YK','Yumiko','Kengaku',0);
/*!40000 ALTER TABLE `da_users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `database_PDB_obs_spr`
--

DROP TABLE IF EXISTS `database_PDB_obs_spr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `database_PDB_obs_spr` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `dep_set_id` varchar(10) NOT NULL,
  `id` varchar(10) DEFAULT NULL,
  `date` datetime DEFAULT NULL,
  `pdb_id` varchar(10) DEFAULT NULL,
  `replace_pdb_id` varchar(10) NOT NULL,
  PRIMARY KEY (`dep_set_id`,`replace_pdb_id`),
  KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `database_PDB_obs_spr`
--

LOCK TABLES `database_PDB_obs_spr` WRITE;
/*!40000 ALTER TABLE `database_PDB_obs_spr` DISABLE KEYS */;
/*!40000 ALTER TABLE `database_PDB_obs_spr` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `database_ref`
--

DROP TABLE IF EXISTS `database_ref`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `database_ref` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `dep_set_id` varchar(10) NOT NULL,
  `database_name` varchar(20) NOT NULL,
  `database_code` varchar(10) NOT NULL,
  PRIMARY KEY (`dep_set_id`,`database_name`),
  KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `database_ref`
--

LOCK TABLES `database_ref` WRITE;
/*!40000 ALTER TABLE `database_ref` DISABLE KEYS */;
/*!40000 ALTER TABLE `database_ref` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `database_related`
--

DROP TABLE IF EXISTS `database_related`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `database_related` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `dep_set_id` varchar(10) NOT NULL,
  `db_name` varchar(10) NOT NULL,
  `details` varchar(200) DEFAULT NULL,
  `content_type` varchar(10) DEFAULT NULL,
  `db_id` varchar(10) NOT NULL,
  PRIMARY KEY (`dep_set_id`,`db_name`,`db_id`),
  KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `database_related`
--

LOCK TABLES `database_related` WRITE;
/*!40000 ALTER TABLE `database_related` DISABLE KEYS */;
/*!40000 ALTER TABLE `database_related` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Temporary table structure for view `dep_instance`
--

DROP TABLE IF EXISTS `dep_instance`;
/*!50001 DROP VIEW IF EXISTS `dep_instance`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `dep_instance` (
  `dep_set_id` varchar(10),
  `pdb_id` varchar(4),
  `dep_initial_deposition_date` date,
  `annotator_initials` varchar(12),
  `dep_deposit_site` varchar(8),
  `dep_process_site` varchar(8),
  `dep_status_code` varchar(5),
  `dep_author_release_status_code` varchar(5),
  `dep_title` varchar(400),
  `dep_author_list` varchar(500),
  `dep_exp_method` varchar(50),
  `dep_status_code_exp` varchar(4),
  `dep_SG_center` varchar(40),
  `inst_ordinal` int(11),
  `inst_id` varchar(10),
  `inst_owner` varchar(50),
  `inst_status` varchar(10),
  `inst_status_timestamp` decimal(20,8),
  `class_id` varchar(10),
  `class_name` varchar(20),
  `class_title` varchar(50),
  `class_author` varchar(50),
  `class_version` varchar(8),
  `class_file` varchar(100)
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Temporary table structure for view `dep_last_instance`
--

DROP TABLE IF EXISTS `dep_last_instance`;
/*!50001 DROP VIEW IF EXISTS `dep_last_instance`*/;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;
/*!50001 CREATE TABLE `dep_last_instance` (
  `dep_set_id` varchar(10),
  `pdb_id` varchar(4),
  `dep_initial_deposition_date` date,
  `annotator_initials` varchar(12),
  `dep_deposit_site` varchar(8),
  `dep_process_site` varchar(8),
  `dep_status_code` varchar(5),
  `dep_author_release_status_code` varchar(5),
  `dep_title` varchar(400),
  `dep_author_list` varchar(500),
  `dep_exp_method` varchar(50),
  `dep_status_code_exp` varchar(4),
  `dep_SG_center` varchar(40),
  `inst_ordinal` int(11),
  `inst_id` varchar(10),
  `inst_owner` varchar(50),
  `inst_status` varchar(10),
  `inst_status_timestamp` decimal(20,8),
  `class_id` varchar(10),
  `class_name` varchar(20),
  `class_title` varchar(50),
  `class_author` varchar(50),
  `class_version` varchar(8),
  `class_file` varchar(100)
) ENGINE=MyISAM */;
SET character_set_client = @saved_cs_client;

--
-- Table structure for table `dep_with_problems`
--

DROP TABLE IF EXISTS `dep_with_problems`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dep_with_problems` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `dep_set_id` varchar(10) NOT NULL,
  `type` varchar(10) NOT NULL,
  `detail` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ordinal`),
  KEY `dep_set_id` (`dep_set_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dep_with_problems`
--

LOCK TABLES `dep_with_problems` WRITE;
/*!40000 ALTER TABLE `dep_with_problems` DISABLE KEYS */;
/*!40000 ALTER TABLE `dep_with_problems` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `deposition`
--

DROP TABLE IF EXISTS `deposition`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `deposition` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `dep_set_id` varchar(10) NOT NULL,
  `pdb_id` varchar(4) NOT NULL,
  `initial_deposition_date` date DEFAULT NULL,
  `annotator_initials` varchar(12) DEFAULT NULL,
  `deposit_site` varchar(8) DEFAULT NULL,
  `process_site` varchar(8) DEFAULT NULL,
  `status_code` varchar(5) DEFAULT NULL,
  `author_release_status_code` varchar(5) DEFAULT NULL,
  `title` varchar(400) DEFAULT NULL,
  `author_list` varchar(500) DEFAULT NULL,
  `exp_method` varchar(50) DEFAULT NULL,
  `status_code_exp` varchar(4) DEFAULT NULL,
  `SG_center` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`dep_set_id`),
  KEY `dep_set_id_index` (`dep_set_id`),
  KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB AUTO_INCREMENT=15951 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `deposition`
--

LOCK TABLES `deposition` WRITE;
/*!40000 ALTER TABLE `deposition` DISABLE KEYS */;
/*!40000 ALTER TABLE `deposition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `engine_monitoring`
--

DROP TABLE IF EXISTS `engine_monitoring`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `engine_monitoring` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `hostname` varchar(32) NOT NULL,
  `total_physical_mem` decimal(10,1) DEFAULT NULL,
  `total_virtual_mem` decimal(12,0) DEFAULT NULL,
  `physical_mem_usage` decimal(10,1) NOT NULL,
  `virtual_mem_usage` decimal(10,1) DEFAULT NULL,
  `cpu_usage` decimal(10,3) NOT NULL,
  `cpu_number` int(30) DEFAULT NULL,
  `ids_set` varchar(255) DEFAULT NULL,
  `status_timestamp` decimal(20,8) DEFAULT NULL,
  PRIMARY KEY (`hostname`),
  KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `engine_monitoring`
--

LOCK TABLES `engine_monitoring` WRITE;
/*!40000 ALTER TABLE `engine_monitoring` DISABLE KEYS */;
/*!40000 ALTER TABLE `engine_monitoring` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `manager_site`
--

DROP TABLE IF EXISTS `manager_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `manager_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(4) NOT NULL,
  `display_name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `manager_site`
--

LOCK TABLES `manager_site` WRITE;
/*!40000 ALTER TABLE `manager_site` DISABLE KEYS */;
/*!40000 ALTER TABLE `manager_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `process_information`
--

DROP TABLE IF EXISTS `process_information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `process_information` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `dep_set_id` varchar(10) NOT NULL,
  `serial_number` int(11) NOT NULL,
  `process_begin` datetime DEFAULT NULL,
  `process_end` datetime DEFAULT NULL,
  `remark` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`dep_set_id`,`serial_number`),
  KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `process_information`
--

LOCK TABLES `process_information` WRITE;
/*!40000 ALTER TABLE `process_information` DISABLE KEYS */;
/*!40000 ALTER TABLE `process_information` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `release_request`
--

DROP TABLE IF EXISTS `release_request`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `release_request` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `dep_set_id` varchar(10) NOT NULL,
  `citation` varchar(100) DEFAULT NULL,
  `release_date` date DEFAULT NULL,
  `PubMed_id` int(11) DEFAULT NULL,
  KEY `dep_set_id` (`dep_set_id`),
  KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `release_request`
--

LOCK TABLES `release_request` WRITE;
/*!40000 ALTER TABLE `release_request` DISABLE KEYS */;
/*!40000 ALTER TABLE `release_request` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sgcenters`
--

DROP TABLE IF EXISTS `sgcenters`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sgcenters` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(4) NOT NULL,
  `verbose_name` varchar(250) NOT NULL,
  PRIMARY KEY (`code`),
  KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB AUTO_INCREMENT=29 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sgcenters`
--

LOCK TABLES `sgcenters` WRITE;
/*!40000 ALTER TABLE `sgcenters` DISABLE KEYS */;
INSERT INTO `sgcenters` VALUES (1,'BIGS','Bacterial targets at IGS-CNRS [BIGS]'),(2,'BSGC','Berkeley Structural Genomics Center [BSGC]'),(3,'BSGI',' Montreal-Kingston Bacterial Structural Genomics Initiative [BSGI]'),(4,'CESG',' Center for Eukaryotic Structural Genomics [CESG]'),(5,'CHTS','Center for High-Throughput Structural Biology [CHTSB]'),(6,'CSGI','Center for Structural Genomics of Infectious Diseases [CSGID]'),(7,'CSMP','Center for Structures of Membrane Proteins [CSMP]'),(8,'ISFI','Integrated Center for Structure and Function Innovation [ISFI]'),(9,'ISPC','Israel Structural Proteomics Center [ISPC]'),(10,'JCSG','Joint Center for Structural Genomics [JCSG]'),(11,'MCSG','Midwest Center for Structural Genomics [MCSG]'),(12,'MSGP','Marseilles Structural Genomics Program @ AFMB [MSGP]'),(13,'NESG','Northeast Structural Genomics Consortium [NESG]'),(14,'NYCO','New York Consortium on Membrane Protein Structure [NYCOMPS]'),(15,'NYSG','New York SGX Research Center for Structural Genomics [NYSGXRC]'),(16,'OCSP','Ontario Centre for Structural Proteomics [OCSP]'),(17,'OPPF',' Oxford Protein Production Facility [OPPF]'),(18,'RIKE','RIKEN Structural Genomics/Proteomics Initiative [RIKEN]'),(19,'S2F','Structure 2 Function Project [S2F]'),(20,'SECS','Southeast Collaboratory for Structural Genomics [SECSG]'),(21,'SGC','Structural Genomics Consortium [SGC]'),(22,'SGPP','Structural Genomics of Pathogenic Protozoa Consortium [SGPP]'),(23,'SGX','SGX Pharmaceuticals [SGX]'),(24,'SPIN','Structural Proteomics in Europe [SPINE]'),(25,'SSGC','Seattle Structural Genomics Center for Infectious Disease [SSGCID]'),(26,'TBSG','TB Structural Genomics Consortium [TBSGC]'),(27,'XMTB','Mycobacterium Tuberculosis Structural Proteomics Project [XMTB]'),(28,'YSG','Paris-Sud Yeast Structural Genomics [YSG]');
/*!40000 ALTER TABLE `sgcenters` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `site`
--

DROP TABLE IF EXISTS `site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `site` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(4) NOT NULL DEFAULT '',
  `verbose_name` varchar(150) DEFAULT NULL,
  PRIMARY KEY (`code`),
  KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `site`
--

LOCK TABLES `site` WRITE;
/*!40000 ALTER TABLE `site` DISABLE KEYS */;
INSERT INTO `site` VALUES (1,'ALL','All site for administration'),(2,'BMRB','BMRM | Biological Magnetic Resonance Bank'),(3,'PDBe','PDBe | Protein Data Bank Europe'),(4,'PDBj','PDBj | Protein Data Bank Japan'),(5,'RCSB','RCSB | Research Collaboratory for Structural Bioinformatics');
/*!40000 ALTER TABLE `site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `status`
--

DROP TABLE IF EXISTS `status`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `status` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `code` varchar(4) NOT NULL,
  `verbose_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`code`),
  KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `status`
--

LOCK TABLES `status` WRITE;
/*!40000 ALTER TABLE `status` DISABLE KEYS */;
INSERT INTO `status` VALUES (1,'AUTH','AUTH [Waiting for Author]'),(2,'HOLD','HOLD [Hold for one year]'),(3,'HPUB','HPUB [Released upon pubblication]'),(4,'OBS','OBS [Obsolete]'),(5,'PROC','PROC [Under processing]'),(6,'REL','REL [Released]'),(7,'REPL','REPL [Replacement Coordinates]'),(8,'WAIT','WAIT [Awaiting Processing]'),(9,'WDRN','WDRN [Withdrawn]');
/*!40000 ALTER TABLE `status` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wf_class_dict`
--

DROP TABLE IF EXISTS `wf_class_dict`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wf_class_dict` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `wf_class_id` varchar(10) NOT NULL,
  `wf_class_name` varchar(20) NOT NULL,
  `title` varchar(50) DEFAULT NULL,
  `author` varchar(50) DEFAULT NULL,
  `version` varchar(8) DEFAULT NULL,
  `class_file` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`wf_class_id`),
  KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wf_class_dict`
--

LOCK TABLES `wf_class_dict` WRITE;
/*!40000 ALTER TABLE `wf_class_dict` DISABLE KEYS */;
INSERT INTO `wf_class_dict` VALUES (7,'AnnMod','AnnotateModule.xml','Added annotation module','T.J.Oldfield','00.01','AnnotateModule.xml'),(1,'Annotate','Annotation.bf.xml','Annotation flow monitor (of DB) workflow','L. Rinaldi','00.01','Annotation.bf.xml'),(2,'LigMod','LigandModule.xml','Annotation flow monitor (of DB) workflow','L. Rinaldi','00.01','LigandModule.xml'),(3,'monDB','MonitorDB.xml','Annotation flow monitor (of DB) workflow','T.J.Oldfield','00.01','MonitorDB.xml'),(4,'popDB','PopulateDB.xml','Populate DB workflow','L. Rinaldi','00.01','PopulateDB.xml'),(9,'PopulateDB','PopulateDB.xml','Populate DB workflow','T.J.Oldfield','00.01','PopulateDB.xml'),(15,'RawCommand','RawCommand','Direct command','T.J.Oldfield','00.01','RawCommand'),(5,'SeqMod','SequenceModule.xml','Demonstration Workflow','L. Rinaldi','00.01','SequenceModule.xml'),(6,'StatMod','StatusModule.xml','Status changes for release','T.J.Oldfield','00.01','StatusModule.xml'),(8,'ValMod','ValidModule.xml','Coordinate validation module','T.J.Oldfield','00.01','ValidModule.xml');
/*!40000 ALTER TABLE `wf_class_dict` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wf_instance`
--

DROP TABLE IF EXISTS `wf_instance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wf_instance` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `wf_inst_id` varchar(10) NOT NULL,
  `wf_class_id` varchar(10) NOT NULL,
  `dep_set_id` varchar(10) NOT NULL,
  `owner` varchar(50) DEFAULT NULL,
  `inst_status` varchar(10) DEFAULT NULL,
  `status_timestamp` decimal(20,8) DEFAULT NULL,
  PRIMARY KEY (`ordinal`),
  KEY `inst_id_index` (`wf_inst_id`) USING BTREE,
  KEY `class_id_index` (`wf_class_id`) USING BTREE,
  KEY `dep_id_index` (`dep_set_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=95463 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wf_instance`
--

LOCK TABLES `wf_instance` WRITE;
/*!40000 ALTER TABLE `wf_instance` DISABLE KEYS */;
/*!40000 ALTER TABLE `wf_instance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wf_instance_last`
--

DROP TABLE IF EXISTS `wf_instance_last`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wf_instance_last` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `wf_inst_id` varchar(10) NOT NULL,
  `wf_class_id` varchar(10) NOT NULL,
  `dep_set_id` varchar(10) NOT NULL,
  `owner` varchar(50) DEFAULT NULL,
  `inst_status` varchar(10) DEFAULT NULL,
  `status_timestamp` decimal(20,8) DEFAULT NULL,
  PRIMARY KEY (`ordinal`),
  KEY `inst_id_index` (`wf_inst_id`) USING BTREE,
  KEY `class_id_index` (`wf_class_id`) USING BTREE,
  KEY `dep_id_index` (`dep_set_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=95136 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wf_instance_last`
--

LOCK TABLES `wf_instance_last` WRITE;
/*!40000 ALTER TABLE `wf_instance_last` DISABLE KEYS */;
/*!40000 ALTER TABLE `wf_instance_last` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wf_reference`
--

DROP TABLE IF EXISTS `wf_reference`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wf_reference` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `dep_set_id` varchar(10) NOT NULL,
  `wf_inst_id` varchar(10) DEFAULT NULL,
  `wf_task_id` varchar(10) DEFAULT NULL,
  `wf_class_id` varchar(10) DEFAULT NULL,
  `hash_id` varchar(20) NOT NULL,
  `value` varchar(20) DEFAULT NULL,
  KEY `dep_set_id` (`dep_set_id`),
  KEY `hash_id` (`hash_id`),
  KEY `wf_inst_id` (`wf_inst_id`),
  KEY `wf_task_id` (`wf_task_id`),
  KEY `wf_class_id` (`wf_class_id`),
  KEY `ordinal` (`ordinal`)
) ENGINE=InnoDB AUTO_INCREMENT=46729 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wf_reference`
--

LOCK TABLES `wf_reference` WRITE;
/*!40000 ALTER TABLE `wf_reference` DISABLE KEYS */;
/*!40000 ALTER TABLE `wf_reference` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `wf_task`
--

DROP TABLE IF EXISTS `wf_task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `wf_task` (
  `ordinal` int(11) NOT NULL AUTO_INCREMENT,
  `wf_task_id` varchar(10) NOT NULL,
  `wf_inst_id` varchar(10) NOT NULL,
  `wf_class_id` varchar(10) NOT NULL,
  `dep_set_id` varchar(10) NOT NULL,
  `task_name` varchar(10) DEFAULT NULL,
  `task_status` varchar(10) NOT NULL,
  `status_timestamp` decimal(20,8) DEFAULT NULL,
  `task_type` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`ordinal`),
  KEY `wf_task_id` (`wf_task_id`),
  KEY `wf_inst_id` (`wf_inst_id`),
  KEY `wf_class_id` (`wf_class_id`),
  KEY `dep_set_id` (`dep_set_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6071411 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `wf_task`
--

LOCK TABLES `wf_task` WRITE;
/*!40000 ALTER TABLE `wf_task` DISABLE KEYS */;
/*!40000 ALTER TABLE `wf_task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Final view structure for view `dep_instance`
--

/*!50001 DROP TABLE IF EXISTS `dep_instance`*/;
/*!50001 DROP VIEW IF EXISTS `dep_instance`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`wf`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `dep_instance` AS select `d`.`dep_set_id` AS `dep_set_id`,`d`.`pdb_id` AS `pdb_id`,`d`.`initial_deposition_date` AS `dep_initial_deposition_date`,`d`.`annotator_initials` AS `annotator_initials`,`d`.`deposit_site` AS `dep_deposit_site`,`d`.`process_site` AS `dep_process_site`,`d`.`status_code` AS `dep_status_code`,`d`.`author_release_status_code` AS `dep_author_release_status_code`,`d`.`title` AS `dep_title`,`d`.`author_list` AS `dep_author_list`,`d`.`exp_method` AS `dep_exp_method`,`d`.`status_code_exp` AS `dep_status_code_exp`,`d`.`SG_center` AS `dep_SG_center`,`wfi`.`ordinal` AS `inst_ordinal`,`wfi`.`wf_inst_id` AS `inst_id`,`wfi`.`owner` AS `inst_owner`,`wfi`.`inst_status` AS `inst_status`,`wfi`.`status_timestamp` AS `inst_status_timestamp`,`wfi`.`wf_class_id` AS `class_id`,`wfcd`.`wf_class_name` AS `class_name`,`wfcd`.`title` AS `class_title`,`wfcd`.`author` AS `class_author`,`wfcd`.`version` AS `class_version`,`wfcd`.`class_file` AS `class_file` from ((`deposition` `d` join `wf_instance` `wfi`) join `wf_class_dict` `wfcd`) where ((`d`.`dep_set_id` = `wfi`.`dep_set_id`) and (`wfi`.`wf_class_id` = `wfcd`.`wf_class_id`)) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

--
-- Final view structure for view `dep_last_instance`
--

/*!50001 DROP TABLE IF EXISTS `dep_last_instance`*/;
/*!50001 DROP VIEW IF EXISTS `dep_last_instance`*/;
/*!50001 SET @saved_cs_client          = @@character_set_client */;
/*!50001 SET @saved_cs_results         = @@character_set_results */;
/*!50001 SET @saved_col_connection     = @@collation_connection */;
/*!50001 SET character_set_client      = utf8 */;
/*!50001 SET character_set_results     = utf8 */;
/*!50001 SET collation_connection      = utf8_general_ci */;
/*!50001 CREATE ALGORITHM=UNDEFINED */
/*!50013 DEFINER=`wf`@`localhost` SQL SECURITY DEFINER */
/*!50001 VIEW `dep_last_instance` AS (select `deposition`.`dep_set_id` AS `dep_set_id`,`deposition`.`pdb_id` AS `pdb_id`,`deposition`.`initial_deposition_date` AS `dep_initial_deposition_date`,`deposition`.`annotator_initials` AS `annotator_initials`,`deposition`.`deposit_site` AS `dep_deposit_site`,`deposition`.`process_site` AS `dep_process_site`,`deposition`.`status_code` AS `dep_status_code`,`deposition`.`author_release_status_code` AS `dep_author_release_status_code`,`deposition`.`title` AS `dep_title`,`deposition`.`author_list` AS `dep_author_list`,`deposition`.`exp_method` AS `dep_exp_method`,`deposition`.`status_code_exp` AS `dep_status_code_exp`,`deposition`.`SG_center` AS `dep_SG_center`,`wf_instance_last`.`ordinal` AS `inst_ordinal`,`wf_instance_last`.`wf_inst_id` AS `inst_id`,`wf_instance_last`.`owner` AS `inst_owner`,`wf_instance_last`.`inst_status` AS `inst_status`,`wf_instance_last`.`status_timestamp` AS `inst_status_timestamp`,`wf_instance_last`.`wf_class_id` AS `class_id`,`wf_class_dict`.`wf_class_name` AS `class_name`,`wf_class_dict`.`title` AS `class_title`,`wf_class_dict`.`author` AS `class_author`,`wf_class_dict`.`version` AS `class_version`,`wf_class_dict`.`class_file` AS `class_file` from ((`deposition` join `wf_instance_last`) join `wf_class_dict`) where ((`deposition`.`dep_set_id` = `wf_instance_last`.`dep_set_id`) and (`wf_instance_last`.`wf_class_id` = `wf_class_dict`.`wf_class_id`))) */;
/*!50001 SET character_set_client      = @saved_cs_client */;
/*!50001 SET character_set_results     = @saved_cs_results */;
/*!50001 SET collation_connection      = @saved_col_connection */;

