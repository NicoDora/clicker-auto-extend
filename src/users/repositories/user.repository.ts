import { HttpException, HttpStatus, Injectable } from '@nestjs/common';
import { User } from 'src/entities/User';
import { EntityManager } from 'typeorm';
import { QueryFailedError } from 'typeorm';

@Injectable()
export class UserRepository {
  constructor(private readonly entityManager: EntityManager) {}

  async createUser(stdNum: string, password: string) {
    try {
      return await this.entityManager.save(User, { stdNum, password });
    } catch (error) {
      if (
        error instanceof QueryFailedError &&
        error.message.includes('ER_DUP_ENTRY')
      ) {
        throw new HttpException('User already exists', HttpStatus.CONFLICT);
      } else {
        console.error(error);
      }
    }
  }
}
