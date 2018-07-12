from Crypto.Cipher import DES3
from Crypto.Hash import SHA256 as SHA #Crypto안의 Hash에서 SHA256을 호출하는데 그이름을 SHA이라 하겠다.


#CBC모드로 암호화를 진행하는데 그과정에서 초기백터가 필요하다.
class myDES():
	def __init__(self, keytext,ivtext):		#클래스의 생성자 객체가 생성되자마자 자동으로 호출되는 메서드
		hash = SHA.new()					#SHA해시 객체를 생성
		hash.update(keytext.encode())		#해시 할 메시지를 입력해주는과정 SHA256.update()는 유니코드 문자열을 인자로 받지 않는다.
		key = hash.digest()					#keytext의 해시값을 key로 지정해준다.
		self.key = key[:24]					#Pycrpyto모듈에서 제공하는 3DES의 키 크기는 16바이트 또는 24바이트
		
		hash.update(ivtext.encode())		#초기백터값을 설정해준다.
		iv = hash.digest()					#초기백터값의 해시값을 iv에 저장
		self.iv = iv[:8]					#3DES는 64비트 암호화 블록 크기를 가지므로 초기화 백터의 값도 마찬가지 64비트 즉,8바이트가 되야한다.
		
		
	def enc(self,plaintext):							#함수의 이름 그대로 enc => encrypt 암호화
		des3 = DES3.new(self.key,DES3.MODE_CBC,self.iv) #myDES클래스의 생성자에 의해 myDES클래스의 객체가 생성되자마자 self.key와 self.iv가 생성되어 사용이가능
		encmsg = des3.encrypt(plaintext.encode()) 		#encode함수의 디폴트값?
		return encmsg
	
	def dec(self,ciphertext):							#enc와 마찬가지로 이름그대로 dec => decrypt 복호화
		des3 = DES3.new(self.key,DES3.MODE_CBC,self.iv)	#운영모드가 CBC이므로 초기화 벡터가 필요하다.
		decmsg = des3.decrypt(ciphertext)
		return decmsg
	
def main():
	keytext = 'samsjang'				#키를 지정해주는 과정의 일부 keytext를 SHA256으로 해시 한다음 3DES의 키의 길이에 맞게 잘라서 쓴다.
	ivtext = '1234'						#본 소스코드에서는 3DES중에서 CBC운영모드를 사용하므로 초기화 벡터의 지정이 필요하다.
	msg = 'python35'					#평문 -> 암호화 과정을 거칠 원래의 문자열
		
		
	myCipher = myDES(keytext,ivtext)	#myCipher은 객체를 의미하면서도 myDES의 인스턴스이다.
	ciphered = myCipher.enc(msg)		#msg(평문)을 암호화해서 cipered라는 변수에 저장하는 과정
	deciphered = myCipher.dec(ciphered)	#바로윗줄의 enc의 인자값으로는 msg를 주어서 암호화를 진행했지만 dec의 인자값으로는 복호화할 자료 즉,암호화된 결과를 넣어준다.
	print('ORIGINAL:\t%s'%msg)		
	print('CIPHERED:\t%s'%ciphered)
	print('DECIPHERED:\t%s'%deciphered)	#평문과 암호화된결과 복호화결과를 출력해주는 과정.
	
		
if __name__ == '__main__':
	main()
