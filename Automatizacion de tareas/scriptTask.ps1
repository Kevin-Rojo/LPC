$scriptSys = New-ScheduledTaskAction -Execute 'I:\FCFM\LPC\Practica15\send_sysinfo.ps1'
$trigger2 = New-ScheduledTaskTrigger -Once -At 02:20pm

Register-ScheduledTask -Action $scriptSys -Trigger $trigger2 -TaskPath "MisTareas" -TaskName "Enviar Sysinfo" -Description "Envio de informacion del sistema"