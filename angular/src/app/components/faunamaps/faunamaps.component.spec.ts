import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FaunamapsComponent } from './faunamaps.component';

describe('FaunamapsComponent', () => {
  let component: FaunamapsComponent;
  let fixture: ComponentFixture<FaunamapsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FaunamapsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FaunamapsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
