import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ShowItemsComponent } from './show-items.component';

describe('ShowItemsComponent', () => {
  let component: ShowItemsComponent;
  let fixture: ComponentFixture<ShowItemsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ShowItemsComponent]
    });
    fixture = TestBed.createComponent(ShowItemsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
