package com.example.minerva;

import android.app.Activity;
import android.app.AlertDialog;
import android.app.AlertDialog.Builder;
import android.content.Context;
import android.content.DialogInterface;
import android.net.ConnectivityManager;
import android.net.NetworkInfo;
import android.os.Bundle;
import android.webkit.WebView;
import android.webkit.WebViewClient;

public class MainActivity extends Activity {

	private WebView webView;
	private Builder builder;
	private AlertDialog alert;

	@Override
	public void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);

		setContentView(R.layout.activity_main);
		webView = (WebView) findViewById(R.id.webView1);
		webView.setWebViewClient(new WebViewClient());
		webView.getSettings().setJavaScriptEnabled(true);

		builder = new Builder(this);
		builder.setTitle("Internet coonection");
		builder.setMessage("Please connect to the internet");
		builder.setCancelable(false);
		builder.setPositiveButton("Ok", new DialogInterface.OnClickListener() {
			public void onClick(DialogInterface dialog, int which) {
				checkConnectionDialog(checkConnection());
			}
		});
		builder.setNegativeButton("Cancel",
				new DialogInterface.OnClickListener() {
					public void onClick(DialogInterface dialog, int which) {
						finish();
						System.exit(0);
					}
				});

		checkConnectionDialog(checkConnection());

	}

	private boolean checkConnection() {
		NetworkInfo networkInfo = ((ConnectivityManager) getSystemService(Context.CONNECTIVITY_SERVICE))
				.getActiveNetworkInfo();
		return (networkInfo != null && networkInfo.isConnected());
	}

	private void checkConnectionDialog(boolean connection) {
		if (!connection) {
			alert = builder.create();
			alert.show();
		} else {
			webView.loadUrl("http://www.google.com");
		}
	}

}
