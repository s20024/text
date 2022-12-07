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