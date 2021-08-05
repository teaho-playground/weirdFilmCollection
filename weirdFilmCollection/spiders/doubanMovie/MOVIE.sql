use test;
CREATE TABLE `MOVIE` (
  `ID` INTEGER not null comment '主键id',
  `TITLE` varchar(100) comment 'title',
  `RATE` NUMERIC(2,1) comment '评分',
  `URL` varchar(200) comment 'url',
  `DIRECTORS` varchar(100) comment 'directors',
  `CASTS` varchar (100) comment 'casts',
  `NUMBER` INTEGER comment  'number',
  `IMDBURL` varchar (200) comment  'imdburl',
  `IMDBRATE`  NUMERIC(2,1),
  `IMDBRATENUMBER`  INTEGER,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8  COMMENT='movie表';
