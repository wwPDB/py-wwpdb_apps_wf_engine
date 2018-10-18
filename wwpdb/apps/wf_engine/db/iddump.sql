-- MySQL dump 10.13  Distrib 5.6.5-m8, for Linux (x86_64)
--
-- Host: pdb-f-linux-5.rutgers.edu    Database: status
-- ------------------------------------------------------
-- Server version	5.6.12-log

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
-- Dumping data for table `deposition`
--
-- WHERE:  dep_set_id = 'D_1100201333'

LOCK TABLES `deposition` WRITE;
/*!40000 ALTER TABLE `deposition` DISABLE KEYS */;
INSERT INTO `deposition` VALUES (17655,'D_1100201333','4P1H','2014-02-26','unknown','RCSB','?','REPL','HPUB','CRYSTAL STRUCTURE OF HH-PGDS WITH WATER DISPLACING INHIBITOR','day, J.e.thorarensen, a.trujillo, j.i.','X-RAY DIFFRACTION','HPUB','?','123456','',NULL,NULL,'oldfield@ebi.ac.uk','DEP');
/*!40000 ALTER TABLE `deposition` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `communication`
--
-- WHERE:  dep_set_id = 'D_1100201333'

LOCK TABLES `communication` WRITE;
/*!40000 ALTER TABLE `communication` DISABLE KEYS */;
INSERT INTO `communication` VALUES (17933,'INSERT','LOAD','D_1100201333',NULL,NULL,'Annotation.bf.xml','INIT','INIT',446746539.88261800,'D_1100201333','Annotate','W_001',NULL,'pdb-hp-linux-2.rcsb.rutgers.edu','FINISHED');
/*!40000 ALTER TABLE `communication` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `wf_instance`
--
-- WHERE:  dep_set_id = 'D_1100201333'

LOCK TABLES `wf_instance` WRITE;
/*!40000 ALTER TABLE `wf_instance` DISABLE KEYS */;
INSERT INTO `wf_instance` VALUES (107588,'W_001','depUpload','D_1100201333','DepositionUpload.xml','exception',446745210.57021100),(107589,'W_002','Annotate','D_1100201333','Annotation.bf.xml','init',446745415.21819800),(107590,'W_003','DepVal','D_1100201333','DepValModule.xml','finished',446745414.07186800);
/*!40000 ALTER TABLE `wf_instance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `wf_task`
--
-- WHERE:  dep_set_id = 'D_1100201333'

LOCK TABLES `wf_task` WRITE;
/*!40000 ALTER TABLE `wf_task` DISABLE KEYS */;
INSERT INTO `wf_task` VALUES (6151249,'T1','W_002','uploadMod','D_1100201333','T1','finished',446745293.93403100,'Entry-point'),(6151250,'TP3','W_002','uploadMod','D_1100201333','TP3','finished',446745295.95627100,'Process'),(6151251,'TP31','W_002','uploadMod','D_1100201333','TP31','finished',446745296.98262700,'Process'),(6151252,'TA32','W_002','uploadMod','D_1100201333','TA32','finished',446745297.00064100,'Decision'),(6151253,'TP5','W_002','uploadMod','D_1100201333','TP5','finished',446745306.03575200,'Process'),(6151254,'TP10','W_002','uploadMod','D_1100201333','TP10','finished',446745414.17971000,'Workflow'),(6151255,'T1','W_003','DepVal','D_1100201333','T1','finished',446745306.83187800,'Entry-point'),(6151256,'TP6','W_003','DepVal','D_1100201333','TP6','finished',446745410.97924900,'Process'),(6151257,'TP31','W_003','DepVal','D_1100201333','TP31','finished',446745411.99929100,'Process'),(6151258,'TA32','W_003','DepVal','D_1100201333','TA32','finished',446745412.01738200,'Decision'),(6151259,'TP5','W_003','DepVal','D_1100201333','TP5','finished',446745413.04175200,'Process'),(6151260,'TP88','W_003','DepVal','D_1100201333','TP88','finished',446745414.06144000,'Process'),(6151261,'T9','W_003','DepVal','D_1100201333','T9','finished',446745414.06800500,'Exit-point'),(6151262,'TP88','W_002','uploadMod','D_1100201333','TP88','finished',446745415.21018600,'Process'),(6151263,'T9','W_002','uploadMod','D_1100201333','T9','finished',446745415.21495500,'Exit-point');
/*!40000 ALTER TABLE `wf_task` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `user_data`
--
-- WHERE:  dep_set_id = 'D_1100201333'

LOCK TABLES `user_data` WRITE;
/*!40000 ALTER TABLE `user_data` DISABLE KEYS */;
INSERT INTO `user_data` VALUES (253,'D_1100201333','oldfield@ebi.ac.uk','h','responsi');
/*!40000 ALTER TABLE `user_data` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `timestamp`
--
-- WHERE:  dep_set_id = 'D_1100201333'

LOCK TABLES `timestamp` WRITE;
/*!40000 ALTER TABLE `timestamp` DISABLE KEYS */;
INSERT INTO `timestamp` VALUES (505,'D_1100201333',1393430033.47,'login','','','',''),(506,'D_1100201333',1393430080.82,'upload','4ec0-demo-sf.cif','D_1100201333_sf-upload_P1.cif.V1','structure-factors','pdbx'),(507,'D_1100201333',1393430081.06,'upload','4ec0.ent','D_1100201333_model-upload_P1.pdb.V1','model','pdb'),(508,'D_1100201333',1393430084.07,'convert','pdb2pdbx-deposit(D_1100201333_model_P1.cif.V1)','D_1100201333_model-upload-convert_P1.cif.V1','model','pdbx'),(509,'D_1100201333',1393430086.93,'convert','pdbxsf2pdbx(D_1100201333_sf_P1.cif.V2)','D_1100201333_sf-upload-convert_P1.cif.V1','structure-factors','pdbx'),(510,'D_1100201333',1393430092.82,'process2','','','',''),(511,'D_1100201333',1393430296.55,'submit1','','','',''),(512,'D_1100201333',1393430299.13,'submit2','','','',''),(514,'D_1100201333',1393430557.72,'login','','','',''),(515,'D_1100201333',1393430559.88,'reset','','','',''),(516,'D_1100201333',1393430560.48,'logout','','','',''),(517,'D_1100201333',1393430632.51,'submit1','','','',''),(518,'D_1100201333',1393430634.94,'submit2','','','',''),(520,'D_1100201333',1393430670.64,'login','','','',''),(521,'D_1100201333',1393430672.32,'reset','','','',''),(522,'D_1100201333',1393430672.93,'logout','','','',''),(523,'D_1100201333',1393430689.30,'submit1','','','',''),(524,'D_1100201333',1393430691.77,'submit2','','','',''),(526,'D_1100201333',1393430786.12,'login','','','',''),(527,'D_1100201333',1393430787.86,'reset','','','',''),(528,'D_1100201333',1393430788.66,'logout','','','',''),(529,'D_1100201333',1393430837.19,'upload','1cbs.cif','D_1100201333_model-upload_P1.cif.V1','model','pdbx'),(530,'D_1100201333',1393431338.46,'submit1','','','',''),(531,'D_1100201333',1393431340.25,'submit2','','','',''),(532,'D_1100201333',1393432623.33,'logout','','','','');
/*!40000 ALTER TABLE `timestamp` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-03-03  7:46:32
