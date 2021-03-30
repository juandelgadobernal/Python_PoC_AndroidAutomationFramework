import { Component, OnInit, Input, Output, EventEmitter } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrls: ['./test.component.less']
})
export class TestComponent implements OnInit {

  @Input() consoleText: string;
  @Output() onConsoleResult = new EventEmitter<string>();
  @Output() onLoading = new EventEmitter<boolean>();
  @Input() apiRoute: string;
  @Input() title: string;
  @Input() description: string;

  baseUrl: string = "http://localhost:5000/";
  
  constructor(private httpClient: HttpClient) { }

  ngOnInit() {
  }

  performTest(): void {
    this.onLoading.emit(true);
    var url: string = this.baseUrl + this.apiRoute;
    this.httpClient.get(url).subscribe((res) => {
      this.consoleText = res.toString();
      this.onConsoleResult.emit(this.consoleText);
      this.onLoading.emit(false);
    });
  }
}