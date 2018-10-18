alter table engine_monitoring change swap swap_total decimal(12,0) ;
alter table engine_monitoring add column swap_used decimal(12,0) default 0;
alter table engine_monitoring add column swap_free decimal(12,0) default 0;
