import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.less']
})
export class AppComponent {
  consoleText: string = "";
  isLoading: boolean = false;
  title = 'gui';

  getConsoleText(consoleText: string) {
    this.consoleText= consoleText;
  }

  getLoading(isLoading: boolean){
    this.isLoading = isLoading;
  }
}
