/**
 * Twitter Bootstrap Look and Feel
 * Based on http://twitter.github.com/bootstrap/
 */
.alertify,
.alertify-log {
	font-family: sans-serif;
}
.alertify {
	background: #FFF;
	border: 1px solid #8E8E8E; /* browsers that don't support rgba */
	border: 1px solid rgba(0,0,0,.3);
	border-radius: 6px;
	box-shadow: 0 3px 7px rgba(0,0,0,.3);
	-webkit-background-clip: padding;     /* Safari 4? Chrome 6? */
	   -moz-background-clip: padding;     /* Firefox 3.6 */
	        background-clip: padding-box; /* Firefox 4, Safari 5, Opera 10, IE 9 */
}
.alertify-dialog {
	padding: 0;
}
	.alertify-inner {
		text-align: left;
	}
		.alertify-message {
			padding: 15px;
			margin: 0;
		}
		.alertify-text-wrapper {
			padding: 0 15px;
		}
			.alertify-text {
				color: #555;
				border-radius: 4px;
				padding: 8px;
				background-color: #FFF;
				border: 1px solid #CCC;
				box-shadow: inset 0 1px 1px rgba(0,0,0,.075);
			}
			.alertify-text:focus {
				border-color: rgba(82,168,236,.8);
				outline: 0;
				box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(82,168,236,.6);
			}

		.alertify-buttons {
			padding: 14px 15px 15px;
			background: #F5F5F5;
			border-top: 1px solid #DDD;
			border-radius: 0 0 6px 6px;
			box-shadow: inset 0 1px 0 #FFF;
			text-align: right;
		}
			.alertify-button,
			.alertify-button:hover,
			.alertify-button:focus,
			.alertify-button:active {
				margin-left: 10px;
				border-radius: 4px;
				font-weight: normal;
				padding: 4px 12px;
				text-decoration: none;
				box-shadow: inset 0 1px 0 rgba(255, 255, 255, .2), 0 1px 2px rgba(0, 0, 0, .05);
				background-image: -webkit-linear-gradient(top, rgba(255,255,255,.3), rgba(255,255,255,0));
				background-image:    -moz-linear-gradient(top, rgba(255,255,255,.3), rgba(255,255,255,0));
				background-image:     -ms-linear-gradient(top, rgba(255,255,255,.3), rgba(255,255,255,0));
				background-image:      -o-linear-gradient(top, rgba(255,255,255,.3), rgba(255,255,255,0));
				background-image:         linear-gradient(top, rgba(255,255,255,.3), rgba(255,255,255,0));
			}
			.alertify-button:focus {
				outline: none;
				box-shadow: 0 0 5px #2B72D5;
			}
			.alertify-button:active {
				position: relative;
				box-shadow: inset 0 2px 4px rgba(0,0,0,.15), 0 1px 2px rgba(0,0,0,.05);
			}
				.alertify-button-cancel,
				.alertify-button-cancel:hover,
				.alertify-button-cancel:focus,
				.alertify-button-cancel:active {
					text-shadow: 0 -1px 0 rgba(255,255,255,.75);
					background-color: #E6E6E6;
					border: 1px solid #BBB;
					color: #333;
					background-image: -webkit-linear-gradient(top, #FFF, #E6E6E6);
					background-image:    -moz-linear-gradient(top, #FFF, #E6E6E6);
					background-image:     -ms-linear-gradient(top, #FFF, #E6E6E6);
					background-image:      -o-linear-gradient(top, #FFF, #E6E6E6);
					background-image:         linear-gradient(top, #FFF, #E6E6E6);
				}
				.alertify-button-cancel:hover,
				.alertify-button-cancel:focus,
				.alertify-button-cancel:active {
					background: #E6E6E6;
				}
				.alertify-button-ok,
				.alertify-button-ok:hover,
				.alertify-button-ok:focus,
				.alertify-button-ok:active {
					text-shadow: 0 -1px 0 rgba(0,0,0,.25);
					background-color: #04C;
					border: 1px solid #04C;
					border-color: #04C #04C #002A80;
					border-color: rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.1) rgba(0, 0, 0, 0.25);
					color: #FFF;
				}
				.alertify-button-ok:hover,
				.alertify-button-ok:focus,
				.alertify-button-ok:active {
					background: #04C;
				}

.alertify-log {
	background: #D9EDF7;
	padding: 8px 14px;
	border-radius: 4px;
	color: #3A8ABF;
	text-shadow: 0 1px 0 rgba(255,255,255,.5);
	border: 1px solid #BCE8F1;
}
	.alertify-log-error {
		color: #B94A48;
		background: #F2DEDE;
		border: 1px solid #EED3D7;
	}
	.alertify-log-success {
		color: #468847;
		background: #DFF0D8;
		border: 1px solid #D6E9C6;
}
