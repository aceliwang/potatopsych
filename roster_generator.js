
// Identify all registrars
class Registrar {
    constructor(leave, availabilities) {
        this.leave = "";
        this.team = "";

    }
}

// Select requested dates
var date_start, date_end;
// Identify all shifts that need to be covered
// Date start = 23/11/24
// Date end = 06/02/24
// Public Holidays = 25/12/24, 26/12/24, 01/01/25, 30/12/24
// Extra Nights = 
// Extra Clozapines = 29/12/24
// // Consider public holidays, extra nights, extra clozapines

class ShiftAllocation {
    constructor() {
        this.registrar = ""
        this.status = "" // locked in or not
    }
}
class Day {
    constructor(date) {
        this.date = date;
        this.day_of_week = date.getDay();
        this.public_hol = false; // TODO
        this.ed_am = "";
        this.ed_pm = "";
        this.ah = "";
        this.short = "";
        this.nights = "";
        this.cloz_am = "";
        this.cloz_pm = "";
        this.ect = "";
        this.sick = "";
    }
}

class Template {
    constructor(registrar, command, day, shift) {
        this.command = command
        this.registrar = registrar
        this.day = day
        this.shift = shift
    }
}



class Roster {
    // new attribute for each shift?
    constructor() {
        this.roster_array = []
        let roster_start = new Date("11/23/24") // note this is american and needs parsing
        let roster_end = new Date("06/02/25")
        console.log(this.roster_array)

        let loop = new Date(roster_start)
        while (loop <= roster_end) {
            console.log(loop);
            let day = new Day(loop);

            switch (loop.getDay()) {
                case 1: // Monday
                case 3: // Wednesday
                case 5: // Friday
                    // ECT, EDAM, EDPM, Sick, After Hours
                    day.cloz_am = null
                    day.cloz_pm = null
                    day.short = null
                    day.nights = null
                    break;
                case 2: // Tuesday
                case 4: // Thursday
                    // Cloz AM, Cloz PM, Sick, After Hours
                    day.ect = null
                    day.short = null
                    day.nights = null
                    break;
                case 6: // Saturday
                    // Night, Fall Through
                    day.ed_am = null
                    day.ed_pm = null
                    day.cloz_am = null
                    day.cloz_pm = null
                    day.ect = null
                    day.sick = null
                case 0: // Sunday
                    // Short Shift, Long Shift
                    day.nights = null
                    break;
            }
            this.roster_array.push(day)

            let newDate = loop.setDate(loop.getDate() + 1);
            loop = new Date(newDate);
        }
        // TODO: if public holiday: Short Shift, Long Shift
        // TODO: add extra nights, add extra clozapines
    }

    process_templates(all_templates) {
        all_templates.forEach((template) => {
            switch (template.command) {
                case "locked_in":
                    this.roster_array.forEach((shift) => {
                        if (shift.day = template.day) {
                            template.shift.registrar = template.registrar
                            shift.status = "template"
                            // TODO: do checks, raise error
                        }
                    })
                    break;
                case "rotates": // todo
                    this.roster_array.forEach((shift) => {

                    })
                    break;
            }
        })
    }
}




// RULES
// No back to back days
// No Fri then Sun
// If FEC, cannot do Cloz PM or ED PM or After Hours
// Stage 3 does not do Sick

// Identify people who want shifts and then eliminate those shifts
// EG: A Darwich LOCKED IN 
// Process templates ie. community does this shift. Targets clozapine and ECT.
// // Two types of templates. Roles are already taken
// EG: North LOCKED IN Cloz Tues AM
// EG: Community LOCKED IN Cloz Thurs PM
// EG: Acute LOCKED IN Cloz Tues AM
// EG: J Norman LOCKED IN Cloz Tues PM


// EG: PECC LOCKED IN ED Thurs AM
// EG: FCMHT LOCKED IN ED Fri PM
// EG: Community LOCKED IN ED Mon PM
// EG: EPIP LOCKED IN ED Tues PM
// EG: North LOCKED IN ED Wed AM

// Rotating templates
// EG: Inpatient ROTATES Cloz Thurs PM
// EG: LVH ROTATES ECT
// EG: CL ROTATES ED Mon Fri AM



// TODO: process preferences

// Identify all people who can do each shift ie. eliminate leave, FEC can't do sick leave, can't do ED PM or cloz PM

// Brute force remaining shifts
// class TempRoster {
//     func detectClashes() {

//     }
//     func calculateHappiness() {

//     }

// }


// Measure fairness AFTER templates
// // ECT should be fairly fair across
// // Clozapine should also be fair after templates
// // After hours needs to be fair, but should take into consideration preferences




// 8 shifts ^ 20 regs

test = new Roster()

// run templates
template = Template("J Norman", "locked in", "Tuesday", "Cloz PM")
test.process_templates[template]

// PRINTING
test.roster_array.forEach(function (item) {
    console.log(item.date, item)
})
