class Event:

    

    def __init__(self, name, date, start_t, end_t, num_vol_required, maxVol):
        self.name = name
        self.date = date
        self.start_t = start_t
        self.end_t = end_t
        self.num_vol_required = num_vol_required
        self.num_vol_registered = 0
        self.maxVol = maxVol
        self.volunteers = []
        self.status = 'Pending Volunteers'
        

    
    def register_volunteer(self, volunteer):
        if self.maxVol > self.num_vol_registered:
            self.volunteers.append(volunteer)
            self.num_vol_registered += 1
            update_status()
            return True
        else:
            return False

    
    def cancel_volunteer(self, volunteer):
        if volunteer in self.volunteers:
            self.volunteers.remove(volunteer)
            self.num_vol_registered -= 1
            update_status(self)
            return True
        else:
            return False

    def view_events(events):
        event_list = []
        for event in events:
            event_data = {}
            event_data['name'] = event.name
            event_data['date'] = event.date
            event_data['start_time'] = event.start_t
            event_data['end_time'] = event.end_t
            event_data['num_vol_required'] = event.num_vol_required
            event_data['num_vol_registered'] = event.num_vol_registered
            event_data['status'] = event.status
            event_list.append(event_data)
        return event_list
    #return render_template('view_events.html', events=event_list)   

    def update_status(self):
        if len(self.volunteers) != self.num_vol_required:
            self.status = 'Pending volunteers'
        
        elif len(self.volunteers) = self.num_vol_required:
            self.status = 'Minimum volunteers met'
        
        elif len(self.volunteers) = self.maxVol:
            self.status = 'Max ' 

        

        

    


