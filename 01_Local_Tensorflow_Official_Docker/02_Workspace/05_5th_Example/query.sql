select 
	tsi||','||ls||','||xp||','||fo||','||stm||','||lo||','||kp||','||df||','||pm||','||wi||','||ps||','||sc||','||sp||','||con||','||wage||','||rt as csv
from 
	player
where 
	date=last
	and po='KP'
order by 
	date,num ;
