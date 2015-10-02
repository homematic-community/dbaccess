#!/bin/tclsh

load tclrega.so
source [file join $env(DOCUMENT_ROOT) once.tcl]
source [file join $env(DOCUMENT_ROOT) cgi.tcl]


cgi_eval {
	
	array set res [rega_script {

		string s_sysvar;
		object o_sysvar;
		foreach (s_sysvar, dom.GetObject (ID_SYSTEM_VARIABLES).EnumUsedIDs()) {
			o_sysvar = dom.GetObject (s_sysvar);
			WriteLine (o_sysvar.ID() # o_sysvar.Timestamp().ToInteger() # "\t" # o_sysvar.ID() # "\t" # o_sysvar.Value() # "\t" # o_sysvar.Timestamp().Format("%F %T") # "\t");
		}

		string s_channel;
		object o_channel;
		string s_dp;
		object o_dp;
		foreach (s_channel, dom.GetObject (ID_CHANNELS).EnumUsedIDs()) {
			o_channel = dom.GetObject (s_channel);
			if (o_channel) {
				foreach (s_dp, o_channel.DPs().EnumUsedIDs()) {
					o_dp = dom.GetObject (s_dp);
					if (o_dp.Operations() & OPERATION_READ) {
						WriteLine (o_dp.ID() # o_dp.Timestamp().ToInteger() # "\t" # o_dp.ID() # "\t" # o_dp.Value() # "\t" # o_dp.Timestamp().Format("%F %T") # "\t");
					}
				}
			} else {
				WriteLine (s_channel # "\t0\t0\t0\t");
			}
		}

	}]
	
	puts -nonewline $res(STDOUT)


}
