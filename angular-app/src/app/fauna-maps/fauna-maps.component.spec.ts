import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FaunaMapsComponent } from './fauna-maps.component';

describe('FaunaMapsComponent', () => {
  let component: FaunaMapsComponent;
  let fixture: ComponentFixture<FaunaMapsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FaunaMapsComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FaunaMapsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
