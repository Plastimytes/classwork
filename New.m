I=imread("pexels-bradikan-30345636.jpg");
I3 = I;
I2 = I;
I1 = I;

I1(:,:,2:3)=0;
RED = I1;

I2(:,:,1:2) =0;
BLUE = I2;

I3(:,:,1:3) =0;
GREEN = I3

figure;
subplot(2,2,1),imshow(I);
subplot(2,2,2),imshow(RED);
subplot(2,2,3),imshow(GREEN);
subplot(2,2,4),imshow(BLUE);

c = 255-RED;
m = 255-GREEN;
y = 255-BLUE;
figure;
subplot(2,2,1),imshow(I);
subplot(2,2,2),imshow(c);
subplot(2,2,3),imshow(m);
subplot(2,2,4),imshow(y);