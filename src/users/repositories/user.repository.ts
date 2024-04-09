import { Injectable } from '@nestjs/common';
import { User } from 'src/entities/User';
import { EntityManager, FindOneOptions } from 'typeorm';

@Injectable()
export class UserRepository {
  constructor(private readonly entityManager: EntityManager) {}

  createUser(stdNum: string, password: string) {
    return this.entityManager.save(User, { stdNum, password });
  }

  findUser(options: FindOneOptions<User>) {
    return this.entityManager.findOne(User, options);
  }

  updateUser(stdNum: string, password: string) {
    return this.entityManager.update(User, { stdNum }, { password });
  }
}
