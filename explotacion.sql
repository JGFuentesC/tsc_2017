create database tsc;
use tsc;
rename table `crime-lat-long` to crimen;

select * from crimen;

select crime,count(*) as casos from crimen
group by crime order by casos desc