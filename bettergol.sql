CREATE DATABASE  IF NOT EXISTS `bettergol`;
USE `bettergol`;

DROP TABLE IF EXISTS `codigos`;
CREATE TABLE `codigos` (
  `id_codigo` varchar(45) NOT NULL,
  `Nombre` varchar(255) NOT NULL,
  `bool1` tinyint(1) DEFAULT NULL,
  `bool2` tinyint(1) DEFAULT NULL,
  `int1` int DEFAULT NULL,
  `int2` int DEFAULT NULL,
  `string1` varchar(255) DEFAULT NULL,
  `string2` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_codigo`)
); 

LOCK TABLES `codigos` WRITE;
UNLOCK TABLES;

DROP TABLE IF EXISTS `perfiles`;
CREATE TABLE `perfiles` (
  `id_perfil` int NOT NULL AUTO_INCREMENT,
  `perfil` varchar(45) NOT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `bool1` tinyint(1) DEFAULT NULL,
  `bool2` tinyint DEFAULT NULL,
  `int1` int DEFAULT NULL,
  `int2` int DEFAULT NULL,
  `string1` varchar(255) DEFAULT NULL,
  `string2` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_perfil`)
);

LOCK TABLES `perfiles` WRITE;
INSERT INTO `perfiles` VALUES (1,'Administrador','2022-10-26 21:46:51','2022-10-26 21:46:51',NULL,NULL,NULL,NULL,NULL,NULL),(2,'Usuario','2022-10-26 21:46:51','2022-10-26 21:46:51',NULL,NULL,NULL,NULL,NULL,NULL);
UNLOCK TABLES;

DROP TABLE IF EXISTS `usuarios`;
CREATE TABLE `usuarios` (
  `id_usuario` int NOT NULL AUTO_INCREMENT,
  `nombre` varchar(255) NOT NULL,
  `apellido` varchar(255) NOT NULL,
  `dni` varchar(255) NOT NULL,
  `celular` varchar(255) NOT NULL,
  `correo` varchar(255) NOT NULL,
  `clave` varchar(255) NOT NULL,
  `terminos` varchar(45) NOT NULL,
  `recuperarpsw` tinyint DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `perfiles_id_perfil` int NOT NULL,
  `codigo` varchar(255) DEFAULT NULL,
  `bool1` tinyint(1) DEFAULT NULL,
  `bool2` tinyint(1) DEFAULT NULL,
  `bool3` tinyint(1) DEFAULT NULL,
  `int1` int DEFAULT NULL,
  `int2` int DEFAULT NULL,
  `int3` int DEFAULT NULL,
  `string1` varchar(255) DEFAULT NULL,
  `string2` varchar(255) DEFAULT NULL,
  `string3` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_usuario`),
  KEY `fk_usuarios_perfiles1_idx` (`perfiles_id_perfil`),
  CONSTRAINT `fk_usuarios_perfiles1` FOREIGN KEY (`perfiles_id_perfil`) REFERENCES `perfiles` (`id_perfil`)
);

LOCK TABLES `usuarios` WRITE;
INSERT INTO `usuarios` VALUES (1,'Admin','Admin','0','0992720315','bettergol593@gmail.com','$2b$12$wANjBptzc0sXpKwGnaBw8O2QVuD06VdnW5CA73RinydSD2FYdzhpe','aceptado',0,'2022-10-26 21:47:32','2022-10-26 21:47:32',1,'',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
UNLOCK TABLES;

DROP TABLE IF EXISTS `pronosticos`;
CREATE TABLE `pronosticos` (
  `id_pronostico` int NOT NULL AUTO_INCREMENT,
  `usuarios_id_usuario` int NOT NULL,
  `A1` varchar(255) DEFAULT NULL,
  `B2` varchar(255) DEFAULT NULL,
  `C1` varchar(255) DEFAULT NULL,
  `D2` varchar(255) DEFAULT NULL,
  `E1` varchar(255) DEFAULT NULL,
  `F2` varchar(255) DEFAULT NULL,
  `G1` varchar(255) DEFAULT NULL,
  `H2` varchar(255) DEFAULT NULL,
  `A2` varchar(255) DEFAULT NULL,
  `B1` varchar(255) DEFAULT NULL,
  `C2` varchar(255) DEFAULT NULL,
  `D1` varchar(255) DEFAULT NULL,
  `E2` varchar(255) DEFAULT NULL,
  `F1` varchar(255) DEFAULT NULL,
  `G2` varchar(255) DEFAULT NULL,
  `H1` varchar(255) DEFAULT NULL,
  `A1B2` varchar(255) DEFAULT NULL,
  `C1D2` varchar(255) DEFAULT NULL,
  `E1F2` varchar(255) DEFAULT NULL,
  `G1H2` varchar(255) DEFAULT NULL,
  `A2B1` varchar(255) DEFAULT NULL,
  `C2D1` varchar(255) DEFAULT NULL,
  `E2F1` varchar(255) DEFAULT NULL,
  `G2H1` varchar(255) DEFAULT NULL,
  `O1O2` varchar(255) DEFAULT NULL,
  `O3O4` varchar(255) DEFAULT NULL,
  `O5O6` varchar(255) DEFAULT NULL,
  `O7O8` varchar(255) DEFAULT NULL,
  `SEMI1` varchar(255) DEFAULT NULL,
  `SEMI2` varchar(255) DEFAULT NULL,
  `PS1PS2` varchar(255) DEFAULT NULL,
  `final` varchar(255) DEFAULT NULL,
  `segundo` varchar(255) DEFAULT NULL,
  `cuarto` varchar(255) DEFAULT NULL,
  `puntos` int DEFAULT NULL,
  `created_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime DEFAULT CURRENT_TIMESTAMP,
  `bool1` tinyint(1) DEFAULT NULL,
  `bool2` tinyint(1) DEFAULT NULL,
  `int1` int DEFAULT NULL,
  `int2` int DEFAULT NULL,
  `string1` varchar(255) DEFAULT NULL,
  `string2` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id_pronostico`),
  KEY `fk_pronosticos_usuarios1_idx` (`usuarios_id_usuario`),
  CONSTRAINT `fk_pronosticos_usuarios1` FOREIGN KEY (`usuarios_id_usuario`) REFERENCES `usuarios` (`id_usuario`)
);

LOCK TABLES `pronosticos` WRITE;
INSERT INTO `pronosticos` VALUES (1,1,'A1','B2','C1','D2','E1','F2','G1','H2','A2','B1','C2','D1','E2','F1','G2','H1','A1B2','C1D2','E1F2','G1H2','A2B1','C2D1','E2F1','G2H1','O1O2','O3O4','O5O6','O7O8','SEMI1','SEMI2','PS1PS2','final','segundo','cuarto',NULL,'2022-10-26 21:48:11','2022-10-26 21:48:11',NULL,NULL,NULL,NULL,NULL,NULL);
UNLOCK TABLES;
