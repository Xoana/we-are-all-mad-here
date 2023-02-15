import { Component, OnInit } from '@angular/core';
import { BehaviorSubject } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { tap } from 'rxjs/operators';
import { Parameters} from './app.config';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit {

  public displayedColumns: string[] = ['number', 'name', 'weight', 'symbol'];
  public previousPageIndex$ = new BehaviorSubject(0);
  public pageIndex$ = new BehaviorSubject(0);
  public itemsPerPage$ = new BehaviorSubject(10);
  public currentPage$ = new BehaviorSubject(1);
  public sortByColumn$ = new BehaviorSubject(null);
  public sortOrder$ = new BehaviorSubject('asc');
  public data$ = new BehaviorSubject(this.fetchData());
  public totalItems$ = new BehaviorSubject(100);
  public pageSizeOptions = [5, 10, 25, 100];
  public searchTerm$ = new BehaviorSubject(null);
	public apiParams$: BehaviorSubject<Parameters> = new BehaviorSubject({
    _page: this.currentPage$.getValue(),
    _limit: this.itemsPerPage$.getValue(),
    _sort: this.sortByColumn$.getValue(),
    _order: this.sortOrder$.getValue()
  });  

  constructor(private http: HttpClient) {}
  
  ngOnInit() {}

  /**
   * Fetch the data.
   * @returns API response
   */
  public fetchData() {

    let params = {
      _page: this.currentPage$.getValue(),
      _limit: this.itemsPerPage$.getValue(),
      _sort: this.sortByColumn$.getValue(),
      _order: this.sortOrder$.getValue()
    }
    if (this.searchTerm$) { params['q'] = this.searchTerm$.getValue() }

    return this.http.get('/api/periodicElements', { params })
    // .pipe(
    //   tap(res => console.log(`res: ${JSON.stringify(res)}`)),
    // )
  }

  /**
   * Get the pagination event.
   * @param event Pagination event; e.g., {previousPageIndex: 0, pageIndex: 0, pageSize: 5, length: 100}
   */
  public getPaginationEvent(event: any) {
    this.itemsPerPage$.next(event.pageSize)
    this.currentPage$.next(event.pageIndex + 1)
    this.data$.next(this.fetchData());
  }

  /**
   * Get search term and initiate search.
   * @param event keyup event
   */
  public getSearchTerm(event: any) {

    if (event.key == 'Enter') {
      this.searchTerm$.next(event.target.value);
      this.data$.next(this.fetchData());
      this.clearSearch()
    }
    this.searchTerm$.subscribe(val => console.log(val))
  }

  /**
   * Clear search; not currently implemented.
   */
  public clearSearch() {
    this.searchTerm$.next(null);
  }

  /**
   * Get the sort event and fetch data.
   * @param event sort event; e.g., {active: 'symbol', direction: 'asc'}
   */
  public getSortEvent(event: any) {
    this.sortByColumn$.next(event.direction == '' ? null : event.active);
    this.sortOrder$.next(event.direction);
    this.data$.next(this.fetchData());
  }

}
