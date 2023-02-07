import { TestBed } from '@angular/core/testing';

import { FieldWorkService } from './fieldwork.service';

describe('FieldWorkService', () => {
  let service: FieldWorkService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(FieldWorkService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
