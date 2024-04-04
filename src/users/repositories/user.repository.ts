import { Injectable } from '@nestjs/common';
import { User } from 'src/entities/User';
import { EntityManager } from 'typeorm';

@Injectable()
export class UserRepository {
  constructor(private readonly entityManager: EntityManager) {}

  createUser(stdNum: string, password: string) {
    return this.entityManager.save(User, { stdNum, password });
  }
}
