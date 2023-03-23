package com.example.loginpage;

import androidx.appcompat.app.AppCompatActivity;
import io.getstream.chat.android.client.ChatClient;
import io.getstream.chat.android.offline.plugin.configuration.Config;
import io.getstream.chat.android.offline.plugin.factory.StreamOfflinePluginFactory;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;

import java.util.Objects;

public class MainActivity extends AppCompatActivity {


    private EditText Name;
    private EditText Password;
    private TextView Info;
    private Button Login;
    private ImageView Profile;
    private int counter = 5;
    private Button Register;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        init();

    }

    private void init(){
        Name = (EditText) findViewById(R.id.ETUsername);
        Password = (EditText) findViewById(R.id.ETPassword);
        Info = (TextView) findViewById(R.id.TVAttemptsLeft);
        Login = (Button) findViewById(R.id.LoginButton);
        Profile = (ImageView) findViewById(R.id.imageView);
        Info.setText("Number of attempts remaining: 5");
        Register = (Button) findViewById(R.id.register);

        Register.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity.this, RegisterPage.class);
                startActivity(intent);
            }
        });

        Login.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String username = Name.getText().toString();
                String password = Password.getText().toString();
                if(validated(username,password)){
                    //String user_chat_token = "wg8ebbdfv74pkrfaqstha627gs3s96s7smr7ehwseaep5v5sn2z56gn5e9auuwhn";
                    Bundle b = new Bundle();
                    b.putString("username",username);
                    Intent intent = new Intent(MainActivity.this, HomePage.class);
                    intent.putExtras(b);
                    startActivity(intent);
                };
            }
        });
    }


    private boolean validated(String userUsername, String userPassword) {
        System.out.println(userUsername);
        System.out.println(userPassword);
        if ((Objects.equals(userUsername, "Admin")) && (Objects.equals(userPassword, "1234"))) {
            System.out.println("Validated!");
            return true;
        }
        else {
            counter--;

            Info.setText("Number of attempts remaining: " + String.valueOf(counter));

            if (counter == 0) {
                Login.setEnabled(false);
            }
        }
        return false;

    }
    public EditText getName() {
        return Name;
    }

    public void setName(EditText name) {
        Name = name;
    }

    public EditText getPassword() {
        return Password;
    }

    public void setPassword(EditText password) {
        Password = password;
    }

    public TextView getInfo() {
        return Info;
    }

    public void setInfo(TextView info) {
        Info = info;
    }

    public Button getLogin() {
        return Login;
    }

    public void setLogin(Button login) {
        Login = login;
    }

    public ImageView getProfile() {
        return Profile;
    }

    public void setProfile(ImageView profile) {
        Profile = profile;
    }

    public int getCounter() {
        return counter;
    }

    public void setCounter(int counter) {
        this.counter = counter;
    }

}