#!/bin/tclsh

load tclrega.so
source [file join $env(DOCUMENT_ROOT) once.tcl]
source [file join $env(DOCUMENT_ROOT) cgi.tcl]


cgi_eval {
	
	cgi_input
	set item ""
	catch { import item }
	set dp ""
	catch { import dp }
	set value ""
	catch { import value }
	set force ""
	catch { import force }

	array set res [rega_script {

		string s_item = "} $item {";
		string s_dp = "} $dp {";
		string s_value = "} $value {";
		string s_force = "} $force {";
	
		if (s_item != "") {
			object o_object = dom.GetObject(s_item);
			if (o_object) {
				if (s_dp != "") {
					o_object = o_object.DPByHssDP(s_dp);
					if (!o_object) {
						WriteLine (s_item # " found, but " # s_dp # " does not exist.");
					}
				}
			} else {
				WriteLine (s_item # " does not exist.");
			}
			if (o_object) {
				if (s_value != "") {
					if ((s_force == "1") || (o_object.Value().ToString() != s_value)) {
						o_object.State (s_value);
					}
				}
				Write (o_object.Value());
			}
		} else {
			WriteLine ("Parameters:");
			WriteLine ("item=[any name or id from rega]");
			WriteLine ("dp=[any datapoint name] (optional)");
			WriteLine ("value=[new value] (optional)");
			WriteLine ("force=1 (optional)");
			WriteLine ("Example: state.cgi?item=Anwesenheit - returns value");
			WriteLine ("         state.cgi?item=Light&dp=STATE&value=1 - turns light on and returns value");
		}
	}]

	puts -nonewline $res(STDOUT)

}
