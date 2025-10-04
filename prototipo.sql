-- Create the schema
CREATE SCHEMA IF NOT EXISTS `prototipo` DEFAULT CHARACTER SET utf8;
USE `prototipo`;

-- Create the Cliente table
CREATE TABLE IF NOT EXISTS `Cliente` (
  `idCliente` INT NOT NULL,
  `Rut` INT NOT NULL,
  `Nom_ap` VARCHAR(45) NOT NULL,
  `Telefono` INT NOT NULL,
  `email` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`idCliente`)
) ENGINE = InnoDB;

-- Create the Mascota table with foreign key to Cliente
CREATE TABLE IF NOT EXISTS `Mascota` (
  `idMas` INT NOT NULL AUTO_INCREMENT,
  `NombreMascota` VARCHAR(45) NOT NULL,
  `Animal` VARCHAR(45) NOT NULL,
  `Raza` VARCHAR(45) NOT NULL,
  `chip` INT NOT NULL,
  `idCliente` INT NULL,
  PRIMARY KEY (`idMas`),
  CONSTRAINT `fk_Mascota_Cliente`
    FOREIGN KEY (`idCliente`)
    REFERENCES `Cliente` (`idCliente`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION
) ENGINE = InnoDB;