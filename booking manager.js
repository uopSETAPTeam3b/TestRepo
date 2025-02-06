// Booking Manager

// Booking data structure
class Booking {
    constructor(mainMember, datetime, duration, roomId) {
        this.mainMember = mainMember;
        this.datetime = datetime;
        this.duration = duration;
        this.roomId = roomId;
        this.authorizedMembers = [];
        this.bookingId = Math.floor(Math.random() * 1000000);

    }
}

// Functions for Booking Manager
class BookingManager {
    constructor() {
        this.bookings = [];
    }

    // Book room
    bookRoom(token, datetime, duration, roomId) {
        if (this.checkToken(token, bookingId) === true && checkValidNewBooking(datetime, duration, roomId) === true) {
            const booking = new Booking(token, datetime, duration, roomId);
            this.bookings.push(booking);
            return 'Room booked successfully';
        } else {
            return 'Invalid token';
        }

      
    }
    checkValidNewBooking(datetime, duration, roomId) {
        return true
    }
    // Cancel room
    cancelRoom(token, bookingId) {
        if (this.checkToken(token, bookingId) === true) {
            const bookingIndex = this.bookings.findBookingIndex(bookingId);
            if (bookingIndex !== null) {
                this.bookings.splice(bookingIndex, 1);
                return 'SUCCESS: Booking cancelled';
            } else {
                return 'ERROR: Booking not found';
            }
            
        } else {
            return 'ERROR: Invalid token';
        }
        
    }

    // checks valid token (Internal function)
    checkToken(token, bookingId) {
        return true
    }

    // Share room
    shareRoom(token, bookingId, memberId) {
        if (this.checkToken(token, bookingId) === true) {
            const bookingIndex = this.bookings.findBookingIndex(bookingId);
            if (bookingIndex !== null) {
                this.bookings[bookingIndex].authorizedMembers.push(memberId);
                return 'SUCCESS: Room shared successfully';
            } else {
                return 'ERROR: Booking not found';
            }
        } else {
            return 'ERROR: Invalid token';
        }    
    }

    // Find booking (Internal function)
    findBookingIndex(bookingId) {
        if (this.bookings.find(booking => booking.id === bookingId)) {
            return this.bookings.findIndex(booking => booking.id === bookingId)
        } else {
            return null;
        }

    }


}