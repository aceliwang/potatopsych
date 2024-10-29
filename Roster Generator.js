
// Identify all registrars
class Registrar {
    constructor(leave, availabilities) {
        
    }
}

// Select requested dates
var date_start, date_end;
// Identify all shifts that need to be covered
// // Consider public holidays, extra nights, extra clozapines
class Roster {
    // new attribute for each shift?
    constructor(shift_identifiers) {
        date_start, date_end = shift_identifiers
        // TODO: if public holiday: Short Shift, Long Shift


        switch (date.getDay()) {
            case 1: // Monday
            case 3: // Wednesday
            case 5: // Friday
            // ECT, EDAM, EDPM, Sick, After Hours
                break;
            case 2: // Tuesday
            case 4: // Thursday
            // Cloz AM, Cloz PM, Sick, After Hours
                break;
            case 6: // Saturday
            // Night, Fall Through
            case 0: // Sunday
            // Short Shift, Long Shift
                break;
        }
        // TODO: add extra nights, add extra clozapines
    }

}

// Identify people who want shifts and then eliminate those shifts
// Process templates ie. community does this shift. Targets clozapine and ECT.
// // Two types of templates. Roles are already taken


// TODO: process preferences

// Identify all people who can do each shift ie. eliminate leave, FEC can't do sick leave, can't do ED PM or cloz PM

// Brute force remaining shifts
class TempRoster {

}


// Measure fairness AFTER templates
// // ECT should be fairly fair across
// // Clozapine should also be fair after templates
// // After hours needs to be fair, but should take into consideration preferences