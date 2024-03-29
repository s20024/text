# ionicの設定

---
### プロジェクトを作成
```shellscript
ionic start
```

# pluginの使用

---
## CapacitorVideoPlayer
> Capacitorでの動画を再生するプラグイン  
git: https://github.com/jepiqueau/capacitor-video-player  
urlの部分がいまだにわからない。httpsからしか取れなかった。assetsからも取ることができないのだろうか。。。

### install
```shellscript
npm install capacitor-video-player
npx cap sync
```

### 使用方法
page.ts
```typescript
import { CapacitorVideoPlayer } from 'capacitor-video-player';

const options = {
  mode: "fullscreen",
  url: "https://example.com/example.mp4",
  playerId: 'vplayer',
  componentTag: 'vplayer',
}

await CapacitorVideoPlayer.initPlayer(options)
  .then((data: any) => {
    this.aplistorage.log(constant.storage_status.success, data);
  })
  .catch((error: any) => {
    this.aplistorage.log(constant.storage_status.error, error);
  });
```
index.html
```html
<div id="vplayer" slot="fixed"></div>
```

## NgxIonicImageViewer
> Ionicでの画像を表示するプラグイン  
git: https://github.com/simongolms/ngx-ionic-image-viewer#readme  
画像を表示するプラグイン

### install
```shellscript
npm install ngx-ionic-image-viewer
```

### 使用方法
app.module.ts
```typescript
import { NgxIonicImageViewerModule } from 'ngx-ionic-image-viewer';
@NgModule({
  imports: [
    NgxIonicImageViewerModule
  ],
})
export class AppModule {}
```

module.ts
```typescript
import { NgxIonicImageViewerModule } from 'ngx-ionic-image-viewer';
@NgModule({
  imports: [
    NgxIonicImageViewerModule
  ],
})
export class HomePageModule {}
```

page.ts
```typescript
import { ModalController } from '@ionic/angular';
import { ViewerModalComponent } from 'ngx-ionic-image-viewer';
export class HomePage {
  constructor(public modalController: ModalController) {}
  async openViewer() {
    const modal = await this.modalController.create({
      component: ViewerModalComponent,
      componentProps: {
        src: "./assets/img/demo.jpg"
      },
      cssClass: 'ion-img-viewer',
      keyboardClose: true,
      showBackdrop: true
    });
    return await modal.present();
  }
}
```

> htmlで記入する場合
index.html
```html
<ion-img-viewer
  title="Demo"
  text="Component"
  scheme="dark"
  src="./assets/img/demo.jpg"
>
</ion-img-viewer>
```

---

## Swiper
> IonicでのSwiper  
使用したもの: https://takblog.site/web/?p=1343
Ionicでのすワイパーほんとは書き方違うかもしれないけど
一応動作するからこちらの書き方でいこう。

### install
```shellscript
npm install swiper
```

### 使用方法
app.module.ts
```typescript
import { SwiperModule } from 'swiper/angular';
@NgModule({
  imports: [
    SwiperModule,
  ],
})
export class AppModule {}
```

page.ts
```typescript
import { Component } from '@angular/core';
import { Swiper, Controller, Thumbs} from 'swiper';
Swiper.use([Controller, Thumbs]);

@Component({
  selector: 'app-templage',
  templateUrl: 'index.html',
  styleUrls: ['style.scss']
})
export class Page {
  constructor() {}
  ionViewDidEnter() {
    const mainSlides = document.querySelectorAll('.main-swiper .swiper-slide');
    const thumbSlides = document.querySelectorAll('.thumb-swiper .swiper-slide');
    const mainSwiper = new Swiper('.main-swiper',{ 
      loop:true,
      loopedSlides:mainSlides.length,
      effect:'fade',    
      fadeEffect:{
        crossFade:true
      }
    });
    const thumbSwiper = new Swiper('.thumb-swiper',{ 
      slidesPerView:'auto',
      spaceBetween:20,
      centeredSlides:true,
      loop:true,
      loopedSlides:thumbSlides.length,
      slideToClickedSlide:true,
      controller:{
        control: mainSwiper
      }
    });
    mainSwiper.controller.control = thumbSwiper;
  }
}
```

index.html
```html
  div.wrapper>div.swiper.main-swiper>div.swiper-wrapper>(div.swiper-slide>div.slide-content>p{slide$})*10^^div.swiper.thumb-swiper>div.swiper-wrapper>(div.swiper-slide>div.slide-content>p{slide$})*10
```

style.scss
```scss
@import 'swiper/scss';
@import '@ionic/angular/css/ionic-swiper';

.wrapper{
  max-width:500px;
  margin:50px auto;
}
.slide-content{
  width: 100%;
  display: flex;
  align-items:center;
  justify-content:center;
  background-color: #ddd;
}
.main-swiper{
  .slide-content{
    height: 300px;    
  }
}
.thumb-swiper{
  margin-top: 20px;
  .swiper-slide{
    width: 100px;
    cursor: pointer;
  }
  .slide-content{
    height: 50px;
  }
}
```

scssでの違いは多分: https://kiomiru.co.jp/blog/coding/swiper-js/
をみた方がいい
