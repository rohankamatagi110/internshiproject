import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root',
})
export class SharedService {
  constructor(private _http: HttpClient) {}

  additems(data: any): Observable<any> {
    return this._http.post('http://127.0.0.1:8000/api/create/', data);
  }

  updateitems(id: number, data: any): Observable<any> {
    return this._http.put(`http://127.0.0.1:8000/api/update/${id}/`, data);
  }

  getitemsList(): Observable<any> {
    return this._http.get('http://127.0.0.1:8000/api/all/');
  }

  deleteitems(id: number): Observable<any> {
    return this._http.delete(`http://127.0.0.1:8000/api/item/${id}/delete/`);
  }
}