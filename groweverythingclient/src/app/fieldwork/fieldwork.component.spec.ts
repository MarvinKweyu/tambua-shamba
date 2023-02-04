import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FieldworkComponent } from './fieldwork.component';

describe('FieldworkComponent', () => {
  let component: FieldworkComponent;
  let fixture: ComponentFixture<FieldworkComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FieldworkComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FieldworkComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
