CREATE DATABASE projectFertImpact_db;
USE projectFertImpact_db;


CREATE TABLE regions (
    `id_region` INT(11) NOT NULL AUTO_INCREMENT,
    `region_name` VARCHAR(50) NOT NULL UNIQUE,
    `code_3` VARCHAR(10) NOT NULL UNIQUE,
    `code_2` VARCHAR(2) NOT NULL UNIQUE,
    PRIMARY KEY (`id_region`)
);

CREATE TABLE fertilizers (
    `id_fertilizer` INT(11) NOT NULL AUTO_INCREMENT,
    `name_fertilizer` VARCHAR(50) NOT NULL UNIQUE,
    PRIMARY KEY (`id_fertilizer`)
);

CREATE TABLE regions_fertilizers (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `id_region` INT(11) NOT NULL,
    `id_fertilizer` INT(11) NOT NULL,
    `year` INT(4) NOT NULL,
    `amount` FLOAT (10),
    `unit` VARCHAR(50),
    PRIMARY KEY (`id`),
    UNIQUE (`id_region`,`id_fertilizer`,`year`),
    FOREIGN KEY (`id_region`) REFERENCES regions(`id_region`),
    FOREIGN KEY (`id_fertilizer`) REFERENCES fertilizers(`id_fertilizer`)
);

CREATE TABLE flora (
    `id_flora` INT(11) NOT NULL AUTO_INCREMENT,
    `name_flora` VARCHAR(50) NOT NULL UNIQUE,
    `irrigation` VARCHAR(50) NOT NULL,
    PRIMARY KEY (`id_flora`)
);

CREATE TABLE regions_fertilizers_flora1 (
    `id` INT(11) NOT NULL AUTO_INCREMENT,
    `id_region` INT(11) NOT NULL,
    `id_fertilizer` INT(11) NOT NULL,
    `id_flora` INT(11) NOT NULL,
    `year` INT(4) NOT NULL,
    `amount` FLOAT (10),
    `unit` VARCHAR(50),
    PRIMARY KEY (`id`),
    UNIQUE (`id_region`,`id_fertilizer`,`id_flora`,`year`),
    FOREIGN KEY (`id_region`) REFERENCES regions(`id_region`),
    FOREIGN KEY (`id_fertilizer`) REFERENCES fertilizers(`id_fertilizer`),
    FOREIGN KEY (`id_flora`) REFERENCES flora(`id_flora`)  
);



LOAD DATA LOCAL INFILE 'utils/fertilizers.csv'
INTO TABLE regions
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@Entity, @Code)
SET region_name = @Entity, code = @Code;

LOAD DATA LOCAL INFILE 'utils/nit_by_flora_ed.csv' 
INTO TABLE fertilizers
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@dummy, @dummy, @dummy, @dummy, `name_fertilizer`, @dummy, @dummy);

INSERT INTO fertilizers (`name_fertilizer`) VALUES ("nitrogen_derived");
INSERT INTO fertilizers (`name_fertilizer`) VALUES ("phosphorous_derived");
INSERT INTO fertilizers (`name_fertilizer`) VALUES ("potassium_derived");

LOAD DATA LOCAL INFILE 'utils/fertilizers.csv'
INTO TABLE regions_fertilizers
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@Entity, @Code, @Year, @nitrogen_derived, @phosphorous_derived, @potassium_derived)
SET id_region = (SELECT id_region FROM regions WHERE region_name = @Entity),
    id_fertilizer = (SELECT id_fertilizer FROM fertilizers WHERE name_fertilizer = 'nitrogen_derived'),
    year = @Year,
    amount = @nitrogen_derived,
    unit = 'kg/hct';

LOAD DATA LOCAL INFILE 'utils/fertilizers.csv'
INTO TABLE regions_fertilizers
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@Entity, @Code, @Year, @nitrogen_derived, @phosphorous_derived, @potassium_derived)
SET id_region = (SELECT id_region FROM regions WHERE region_name = @Entity),
    id_fertilizer = (SELECT id_fertilizer FROM fertilizers WHERE name_fertilizer = 'phosphorous_derived'),
    year = @Year,
    amount = @phosphorous_derived,
    unit = 'kg/hct';

LOAD DATA LOCAL INFILE 'utils/fertilizers.csv'
INTO TABLE regions_fertilizers
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@Entity, @Code, @Year, @nitrogen_derived, @phosphorous_derived, @potassium_derived)
SET id_region = (SELECT id_region FROM regions WHERE region_name = @Entity),
    id_fertilizer = (SELECT id_fertilizer FROM fertilizers WHERE name_fertilizer = 'potassium_derived'),
    year = @Year,
    amount = @potassium_derived,
    unit = 'kg/hct';

LOAD DATA LOCAL INFILE 'utils/nit_by_flora_ed.csv'
INTO TABLE flora
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@dummy, @Species, @dummy, @dummy, @dummy, @dummy, @Water)
SET name_flora = @Species, irrigation = @Water;

LOAD DATA LOCAL INFILE 'utils/nit_by_flora_ed.csv'
INTO TABLE regions_fertilizers_flora
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@Id, @Species, @Year, @Country, @Nitrates, @Nrates_kg_ha, @Water)
SET id_region = (SELECT id_region FROM regions WHERE region_name = @Country),
    id_fertilizer = (SELECT id_fertilizer FROM fertilizers WHERE name_fertilizer = @Nitrates),
    id_flora = (SELECT id_flora FROM flora WHERE name_flora = @Species),
    year = @Year,
    amount = @Nrates_kg_ha,
    unit = 'kg/hct';

LOAD DATA LOCAL INFILE 'utils/nit_by_flora_ed.csv'
INTO TABLE regions_fertilizers_flora
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@Id, @Species, @Year, @Country, @Nitrates, @Nrates_kg_ha, @Water)
SET id_region = (SELECT id_region FROM regions WHERE region_name = @Country),
    id_fertilizer = (SELECT id_fertilizer FROM fertilizers WHERE name_fertilizer = @Nitrates),
    id_flora = (SELECT id_flora FROM flora WHERE name_flora = @Species),
    year = @Year,
    amount = @Nrates_kg_ha,
    unit = 'kg/hct';


LOAD DATA LOCAL INFILE 'utils/codes_iso.csv'
INTO TABLE regions_temp
FIELDS TERMINATED BY ',' 
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@name, @alpha_2)
SET r.name = (SELECT region_name FROM regions WHERE region_name = @name), 
    code_iso2 = @alpha_2;


LOAD DATA LOCAL INFILE 'utils/fertilizers_regions.csv'
INTO TABLE regions1
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(@Entity, @Code, @dummy, @dummy, @dummy, @dummy ,@alpha_2)
SET region_name = @Entity, code_3 = @Code, code_2 = @alpha_2;





INSERT INTO regions_fertilizers_flora VALUES (5000,7,1,1,1994,25,"HTC");
