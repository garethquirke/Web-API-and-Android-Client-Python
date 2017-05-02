package ca3.guitarstockapp;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.widget.EditText;
import android.widget.TextView;

import java.util.ArrayList;

public class MainActivity extends AppCompatActivity {


    public ArrayList<Guitar> Guitars = new ArrayList<Guitar>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // make volley call inflate array list of type guitar
        // create list view from this
        // allow functions for when a row is clicked

        Guitars.add(new Guitar(1, true, "fender", "guitar", 9));

        TextView name = (TextView) findViewById(R.id.guitarname);
        TextView stock = (TextView) findViewById(R.id.guitarstock);

        name.setText("test");
        stock.setText("another test");



    }
}
